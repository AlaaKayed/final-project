from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db import models
from .Consistancy.Consistancy import BookStoreConsistancyManager

primary_server = 'catalog-instance1:9000'

# Create your views here.
consistancy_manager = BookStoreConsistancyManager(primary_server)


@api_view(['GET'])
def search_book_by_topic(request, topic):

    '''
    search_book_by_topic Function:
        search for books with a specific topic

        Parameter:
            topic : book topic


        Return:
            returns array of books with the specified topic    
    '''

    try:
        selected_books = Book.objects.filter(topic=topic)

        if not selected_books.exists():
            return Response({
                "Message": "There is no book available with the specified topic",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(selected_books, many=True)
   
        return Response(serializer.data)

    except:
        return Response({
            "error": "An Error occured please try again later",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def book_details(request, pk):

    '''
    book_details Function:
        view specific book details

        Parameter:
            pk : book id

        Return:
            returns book details for the given id    
    
    '''

    try:
        selected_book = Book.objects.get(pk=pk)

        serializer = BookSerializer(selected_book, many=False)
        return Response(serializer.data)

    except Book.DoesNotExist:
        return Response({
            "error": "There is no book available with the specified id",
        }, status=status.HTTP_404_NOT_FOUND)

    except:
        return Response({
            "error": "An Error occured please try again later",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_books_number(request, pk):
    book = Book.objects.get(pk=pk)
    book.number_of_items -= 1
    book.save()
    return Response({
        "Message": "Book updated successfully",
    })


@api_view(['PUT'])
def decrement_number_of_items(request, pk):
    '''
    decrement_number_of_items Function
        decrement number of items available for
        this book 

        Parameter:
            pk : book id

        Return :
            returns a successfull message if the book is updated successfully

    '''

    try:
        consistancy_manager.forward_decrement_request(pk)

    except Book.DoesNotExist:
        return Response({
            "error": "There is no book available with the specified id",
        }, status=status.HTTP_404_NOT_FOUND)

    except:
        return Response({
            "error": "An Error occured please try again later",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

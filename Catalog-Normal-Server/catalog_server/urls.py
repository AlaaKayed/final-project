from django.urls import path
from .views import search_book_by_topic, book_details, decrement_number_of_items, update_books_number

urlpatterns = [
    path('search/<str:topic>', search_book_by_topic, name='search_by_topic'),
    path('info/<int:pk>', book_details, name='book-details'),
    path('decrement/<int:pk>', decrement_number_of_items, name='decrement_books_number'),
    path('update/<int:pk>', update_books_number, name='update_books_number')
]
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'topic': {'read_only': True},
            'title': {'read_only': True},
        }

     
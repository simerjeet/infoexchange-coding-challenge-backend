from rest_framework import serializers

from books import models
from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']




class BookNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'author', 'author_id']


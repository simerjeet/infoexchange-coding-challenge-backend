from rest_framework import serializers

from books import models
from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'author']


class BookNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name']


class BookDetailsSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_author')

    def get_author(self, book):
        print(f'book : {book}')
        qs = Author.objects.filter(id=book.author.id)
        serializer = AuthorSerializer(instance=qs, read_only=True, many=True)
        return serializer.data

    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'author']


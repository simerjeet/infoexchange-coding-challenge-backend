from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from books import models, serializers

# * **POST /author/** - Creates a new author with the specified details - Expects a JSON body
# * **GET /author/{{id}}/** - Returns a detail view of the specified author id
# * **PUT /author/{{id}}** - Updates an existing author - Expects a JSON body
from books.utils import CustomModelViewSet


class AuthorAPI(CustomModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = (permissions.AllowAny,)


# * **GET /authors/** - Returns a list of authors in the database in JSON format

class AuthorListAPI(viewsets.ReadOnlyModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = (permissions.AllowAny,)


# * **GET /books/** - Returns a list of books in the database in JSON format
class BooksNameListAPI(viewsets.ReadOnlyModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookNameSerializer
    permission_classes = (permissions.AllowAny,)


# * **GET /book/{{id}}/** - Returns a detail view of the specified book id. Nest author details in JSON format
# * **PUT /book/{{id}}** - Updates an existing book - Expects a JSON body

class BookAPI(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.AllowAny,)


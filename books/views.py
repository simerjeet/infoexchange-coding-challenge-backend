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
class BooksNameAPI(viewsets.ReadOnlyModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookNameSerializer
    permission_classes = (permissions.AllowAny,)


# * **POST /book/** - Creates a new book with the specified details - Expects a JSON body
class BookAPI(APIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if request.data is not None:
            try:
                name = request.data['name']
                isbn = request.data['isbn']
                author_id = request.data['author']

            except KeyError:
                return Response({'message': 'missing required data '}, status.HTTP_400_BAD_REQUEST)

        author = models.Author.objects.get(id=author_id)
        book = models.Book.objects.create(name=name,
                                          isbn=isbn,
                                          author=author)
        serialized_book = self.serializer_class(book)
        return Response(serialized_book.data, status=status.HTTP_201_CREATED)


# * **GET /book/{{id}}/** - Returns a detail view of the specified book id. Nest author details in JSON format
class BookDetailsAPI(viewsets.ReadOnlyModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookDetailsSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return self.queryset.filter(id=book_id)

# * **PUT /book/{{id}}** - Updates an existing book - Expects a JSON body

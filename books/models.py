import uuid

from django.db import models

# Create your models here.
from django.db.models import Model


class Author(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.TextField()
    last_name = models.TextField()


class Book(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    isbn = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from books import views

router = routers.DefaultRouter()

router.register(r'author', views.AuthorAPI)
router.register(r'authors', views.AuthorListAPI)
router.register(r'book', views.BookAPI)
router.register(r'books', views.BooksNameListAPI)

urlpatterns = [
    url(r'', include(router.urls)),
]

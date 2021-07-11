from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from books import views

router = routers.DefaultRouter()

router.register(r'author', views.AuthorAPI)
router.register(r'authors', views.AuthorListAPI)
router.register(r'book/(?P<book_id>[0-9a-f-]{36})', views.BookDetailsAPI)
router.register(r'books', views.BooksNameAPI)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^book/', views.BookAPI.as_view()),
]

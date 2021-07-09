from django.contrib import admin
import books.models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'isbn', 'author']


admin.site.register(books.models.Author, AuthorAdmin)
admin.site.register(books.models.Book, BookAdmin)

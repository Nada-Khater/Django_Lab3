from django.contrib import admin

# Register your models here.

from books.models import Book,Author

admin.site.register(Book)

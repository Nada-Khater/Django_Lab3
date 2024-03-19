from django.urls import path
from books.views import *

urlpatterns = [
    path('<int:id>', profile, name='books.profile'),
    path('land', landing, name='books.land'),
    path('home', home, name='books.home'),
    path('index', books_index, name='books.index'),
    path('index/<int:id>', books_show, name='books.show'),
    path('create', create_book, name='books.create'),
    path('index/<int:id>/delete', delete_book, name='books.delete'),
    path('index/<int:id>/edit', edit_book, name='books.edit'),

    path('displayall', authors_index, name='authors.index'),
    path('addauthor', add_author, name='author.add'),
    path('showauthors/<int:id>', author_show, name='author.show'),
    path('authors/<int:id>/delete', delete_author, name='author.delete'),
    path('editauthor/<int:id>/edit', edit_author, name='author.edit')
] 
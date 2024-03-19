from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from books.models import Book, Author
from books.forms import AuthorModelForm, BookModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.

books= [
		{"id":1, "name":"book1", "price":"100$", "author":"author1", "npages":"100", "image":"pic1.png"},
		{"id":2, "name":"book2", "price":"150$", "author":"author2", "npages":"150", "image":"pic2.png"},
		{"id":3, "name":"book3", "price":"200$", "author":"author3", "npages":"200", "image":"pic4.png"}
	]

def profile(request , id ):
    filtered_books = filter(lambda book: book["id"] == id, books)
    filtered_books = list(filtered_books)
    print(filtered_books)
    if filtered_books:
        # return HttpResponse(filtered_books[0].values())
        return render(request,
                      'profile.html',
                      context= {"book":filtered_books[0]})
    return HttpResponse("book not found")

def landing(request):
    return render(request, "landing.html", context={"books":books})

def home(request):
    return render(request, "home.html")

def books_index(request):
    books_idx = Book.objects.all()
    return render(request, 'index.html', context={"books":books_idx})


# -------------------------------------------- Book CRUD -------------------------------------------- #

def books_show(request, id):
    books_sh = Book.objects.get(id=id)
    author_id = books_sh.author_id
    return render(request, 'show.html', context={"book": books_sh, "author_id": author_id})

# def create_book(request):
#     return render(request, 'create.html')

@login_required(login_url='/users/login/')
def create_book(request):
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            url = reverse("books.index")
            return redirect(url)
    else:
        form = BookModelForm()

    return render(request, 'forms/createbook.html', context={'form': form})

@login_required(login_url='/users/login/')
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    url = reverse("books.index")
    return redirect(url)

@login_required(login_url='/users/login/')
def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.index')
    else:
        form = BookModelForm(instance=book)
    
    return render(request, 'forms/editbook.html', context={'form': form, 'book': book})

# -------------------------------------------- Author CRUD -------------------------------------------- #

def authors_index(request):
    authors = Author.get_all_authors()
    return render(request, "displayall.html", context={"authors": authors})

def author_show(request, id):
    author=Author.get_author_by_id(id)
    books = author.books.all()
    return render(request, 'showauthor.html', context={"author": author, "books": books})

@login_required(login_url='/users/login')
def add_author(request):
    form = AuthorModelForm()
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            url = reverse("authors.index")
            return redirect(url)
    
    # request GET
    return render(request, 'forms/create.html', context={"form":form})

@login_required(login_url='/users/login')
def edit_author(request, id):
    author = Author.get_author_by_id(id)
    form = AuthorModelForm(instance=author) 
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            url = reverse("authors.index")
            return redirect(url)

    # request GET
    return render(request, 'forms/edit.html', context={"form":form})

@login_required(login_url='/users/login')
def delete_author(request, id):
    author =Author.get_author_by_id(id)
    author.delete()
    url = reverse("authors.index")
    return redirect(url)


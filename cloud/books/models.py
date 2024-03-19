from django.db import models
from django.shortcuts import reverse, get_object_or_404

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bdate = models.DateField()
    image = models.ImageField(upload_to='books/images/', null=True)

    def __str__(self):
        return self.name
    
    @property
    def logo_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_url(self):
        return reverse("author.show", args=[self.id])
    
    @classmethod
    def get_all_authors(cls):
        return cls.objects.all()
    
    @classmethod
    def get_author_by_id(cls, id):
        return get_object_or_404(cls, id=id)
    
    @classmethod
    def create_object(cls, **kwargs):
        try:
            author = cls(**kwargs)
            author.save()
        except Exception as e:
            print(e)
            return False
        else:
            return author
        
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    npages = models.IntegerField(null=True)
    image = models.ImageField(upload_to='books/images/', null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @classmethod
    def create_object(cls, **kwargs):
        try:
            book = cls(**kwargs)
            book.save()
        except Exception as e:
            print(e)
            return False
        else:
            return book
    
    @classmethod
    def get_book_by_id(cls, id):
        return get_object_or_404(cls, id=id)

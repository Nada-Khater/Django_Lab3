from django import forms
from books.models import Author, Book

# class AuthorForm(forms.Form):
    # name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Enter your name", max_length=100)
    # image = forms.ImageField(label='image')
    # bdate = forms.DateField(label='bdate', widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Enter your birth date")

# define validation rule for all fields
# def clean_email(self):
#     email= self.cleaned_data['email']
#     # check if email exists before ? return to page --> display form errors

#     if Book.objects.filter(email=email).exists():
#         raise forms.ValidationError("Email already exists")

#     return email

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model= Author
        fields='__all__'
    
    def clean_name(self):
        name= self.cleaned_data['name']
        if len(name) < 2:
                raise forms.ValidationError("Name must be at least 2 characters ")
        return name
    

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_name(self):
        name= self.cleaned_data['name']
        if len(name) < 2:
                raise forms.ValidationError("Name must be at least 2 characters ")
        return name


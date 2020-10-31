from django import forms

from myapi.models import Book

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'count']
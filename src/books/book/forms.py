from book.models import Book

from django import forms


class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title', 'year')

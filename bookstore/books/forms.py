from django import forms
from .models import Book


# creating a form
class BookForm(forms.ModelForm):

    class Meta:
        model = Book

        fields = [
            "name",
            "author",
            "price",
        ]

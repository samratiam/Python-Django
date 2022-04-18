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
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
        }

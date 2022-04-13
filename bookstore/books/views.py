from django.shortcuts import render

from .models import Book
from .forms import BookForm


def create_view(request):
    context = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}

    context["dataset"] = Book.objects.all()

    return render(request, "list_view.html", context)

from django.shortcuts import render
from books.models import Book
from .serializers import BookSerializer

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView, ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreate(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieve(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdate(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDestroy(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListCreate(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
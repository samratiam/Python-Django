from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.views import APIView

class BookAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        
        book = Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id = pk
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.errors,status==status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        id = pk
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id = pk
        book = Book.objects.get(pk=id)
        book.delete()
        return Response({'msg':'Data deleted'})
        
                        
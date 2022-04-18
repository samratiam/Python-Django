from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from .models import Book
from .forms import BookForm

#This class will Add new item and Show All items
class AddShowView(TemplateView):
    template_name = "bookstore/dashboard.html"
    #For GET method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bookform = BookForm()
        books = Book.objects.all()
        context={'books':books,'form':bookform}
        return context 

    #For POST method
    def post(self,request):
        fm = BookForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            price = fm.cleaned_data['price']
            author = fm.cleaned_data['author']
            book = Book(name=name,price=price,author=author)
            book.save()
        return HttpResponseRedirect('/')

class BookDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Book.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)
    
class BookUpdateView(View):
    def get(self,request,id):
        book = Book.objects.get(pk=id)
        form = BookForm(instance=book)
        return render(request, 'bookstore/update.html',{'form':form})
    
    def post(self,request,id):
        book = Book.objects.get(pk=id)
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
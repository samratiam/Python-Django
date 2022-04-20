from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm
from .models import Post

class Create(CreateView):
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = '/blogs/list/'

class List(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = 'data'


    

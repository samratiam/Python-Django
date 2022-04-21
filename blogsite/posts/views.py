from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm
from .models import Post

class Create(CreateView):
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = '/blogs/'



def blogs(request):
    blogs = Post.objects.all()
    data = {'blogs':blogs}
    return render(request,'blogs.html',data)

def blog_details(request,id):
    blog = Post.objects.get(pk=id)
    data = {'blog':blog}
    return render(request,'blog-details.html',data) 

def update(request, id):
    context = {}

    obj = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("home")

    context["form"] = form

    return render(request, "posts/update.html", context)


def delete(request, id):

    context = {}

    obj = get_object_or_404(Post, id=id)

    if request.method == "POST":
        obj.delete()

        return redirect("home")

    return render(request, "posts/delete.html", context)
    




    

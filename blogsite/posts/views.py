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

def blog_details(request,slug):
    blog = Post.objects.get(slug=slug)
    data = {'blog':blog}
    return render(request,'blog-details.html',data) 

def update(request, slug):
    context = {}

    obj = get_object_or_404(Post, slug=slug)

    form = PostForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("blogs")

    context["form"] = form

    return render(request, "posts/update.html", context)


def delete(request, slug):

    context = {}

    obj = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        obj.delete()

        return redirect("blogs")

    return render(request, "posts/delete.html", context)

# def search(request):
#     keyword = request.GET['keyword']
#     if keyword:
#         posts = Post.objects.filter(title__icontains="keyword")
#         return render(request,"search.html",data)




    

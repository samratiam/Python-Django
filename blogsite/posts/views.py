from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

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

@login_required
def update(request, slug):
    context = {}
    
    obj = get_object_or_404(Post, slug=slug, user__id=request.user.id)
    

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

def search(request):
    blogs = Post.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            blogs = blogs.filter(title__icontains=keyword)
        data = {'blogs':blogs}
        return render(request,"posts/search.html",data)
    else:
        return HttpResponse("No results found")




    

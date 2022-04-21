from django.urls import path,include
from . import views
from .views import Create

urlpatterns = [
    path("",views.blogs,name="blogs"),
    path("blog-details/<slug:slug>/",views.blog_details,name="blog_details"),
    path("create/",Create.as_view(),name="create"),
    path("update/<slug:slug>/",views.update,name="update"),
    path("delete/<slug:slug>/",views.delete,name="delete"),
    path("search/",views.search,name="search"),
]


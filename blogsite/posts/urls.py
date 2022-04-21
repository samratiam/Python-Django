from django.urls import path,include
from . import views
from .views import Create

urlpatterns = [
    path("",views.blogs,name="blogs"),
    path("blog-details/<slug:slug>/",views.blog_details,name="blog_details"),
    path("create/",Create.as_view(),name="create"),
    path("update/<int:id>/",views.update,name="update"),
    path("delete/<int:id>/",views.delete,name="delete"),

]


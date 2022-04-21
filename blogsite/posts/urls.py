from django.urls import path,include
from . import views
from .views import Create

urlpatterns = [
    path("",views.blogs,name="home"),
    path("blog-details/<int:id>/",views.blog_details,name="blog-details"),
    path("create/",Create.as_view(),name="create"),
    path("update/<int:id>/",views.update,name="update"),
    path("delete/<int:id>/",views.delete,name="delete"),

]


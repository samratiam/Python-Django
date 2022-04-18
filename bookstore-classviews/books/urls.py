from django.urls import path, include
from . import views
from django.views.generic.list import ListView
from .models import Book

urlpatterns = [
    
    #Class based views
    path('', views.AddShowView.as_view(),name="dashboard"),
    path('delete-book/<int:id>/', views.BookDeleteView.as_view(),name="delete"),
    path('update-book/<int:id>/', views.BookUpdateView.as_view(),name="update")
    
]

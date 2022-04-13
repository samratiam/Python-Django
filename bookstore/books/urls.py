from django.urls import path, include
from . import views

urlpatterns = [
    path('create-view/', views.create_view),
    path('list-view/', views.list_view),
]

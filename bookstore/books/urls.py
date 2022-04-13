from django.urls import path, include
from . import views

urlpatterns = [
    path('create-view/', views.create_view),
    path('list-view/', views.list_view),
    path('update-view/<id>/', views.update_view),
    path('<id>/', views.detail_view),
]

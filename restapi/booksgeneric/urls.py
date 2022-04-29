from . import views

from django.urls import path

urlpatterns = [
    path('',views.BookList.as_view()),
    path('create/',views.BookCreate.as_view()),
    path('retrieve/<int:pk>/',views.BookRetrieve.as_view()),
    path('update/<int:pk>/',views.BookUpdate.as_view()),
    path('destroy/<int:pk>/',views.BookDestroy.as_view()),
    
    path('listcreate/',views.BookListCreate.as_view()),
    path('retrieveupdate/<int:pk>/',views.BookRetrieveUpdate.as_view()),
    path('retrievedestroy/<int:pk>/',views.BookRetrieveDestroy.as_view()),
    path('retrieveupdatedestroy/<int:pk>/',views.BookRetrieveUpdateDestroy.as_view()),
]
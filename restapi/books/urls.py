from django.urls import path,include

from books.viewset_views import BookModelViewSet
from . import views

from rest_framework.routers import DefaultRouter

r = DefaultRouter()
r.register('view-set',BookModelViewSet)

urlpatterns = [
    path('bookapi/',views.BookAPI.as_view()),
    path('bookapi/<int:pk>/',views.BookAPI.as_view()),
    
    #One way to use ModelViewSet for get and post method
    # path('view-set/',BookModelViewSet.as_view(actions={'get':'list','post':'create'})),
    
] + r.urls
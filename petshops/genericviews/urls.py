from django.urls import path
from .views import  LocationListCreateAPIView,LocationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('locations/',LocationListCreateAPIView.as_view()),
    path('locations/<int:pk>/',LocationRetrieveUpdateDestroyAPIView.as_view())
]

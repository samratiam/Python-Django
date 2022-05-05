from django.urls import path
from .views import *


urlpatterns = [
    path('locations/',LocationListCreateAPIView.as_view()),
    path('locations/<int:pk>/',LocationRetrieveUpdateDestroyAPIView.as_view()),
    path('petstores/',PetstoreListCreateAPIView.as_view()),
    path('petstores/<int:pk>/',PetstoreRetrieveUpdateDestroyAPIView.as_view()),
    path('categories/',CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/',CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('breeds/',BreedListCreateAPIView.as_view()),
    path('breeds/<int:pk>/',BreedRetrieveUpdateDestroyAPIView.as_view()),
    path('employees/',EmployeeListCreateAPIView.as_view()),
    path('employees/<int:pk>/',EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    path('customers/',CustomerListCreateAPIView.as_view()),
    path('customers/<int:pk>/',CustomerRetrieveUpdateDestroyAPIView.as_view()),
    path('sales/',SaleListCreateAPIView.as_view()),
    path('sales/<int:pk>/',SaleRetrieveUpdateDestroyAPIView.as_view()),
]

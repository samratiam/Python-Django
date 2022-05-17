from django.urls import path,include
from .views import LocationModelViewSet,PetstoreModelViewSet,CategoryModelViewSet, BreedModelViewSet,EmployeeModelViewSet,CustomerModelViewSet,SaleModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'locations',LocationModelViewSet,basename='location')
router.register(r'petstores',PetstoreModelViewSet,basename='petstore')
router.register(r'categories',CategoryModelViewSet,basename='category')
router.register(r'breeds',BreedModelViewSet,basename='breed')
router.register(r'employees',EmployeeModelViewSet,basename='employee')
router.register(r'customers',CustomerModelViewSet,basename='customer')
router.register(r'sales',SaleModelViewSet,basename='sale')
urlpatterns = [
    path("",include(router.urls)),
]
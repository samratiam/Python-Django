from django.urls import path,include
from .views import LocationViewSet,PetstoreViewSet,CategoryViewSet, BreedViewSet,EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'locations',LocationViewSet,basename='location')
router.register(r'petstores',PetstoreViewSet,basename='petstore')
router.register(r'categories',CategoryViewSet,basename='category')
router.register(r'breeds',BreedViewSet,basename='breed')
router.register(r'employees',EmployeeViewSet,basename='employee')
urlpatterns = [
    path("",include(router.urls)),
]

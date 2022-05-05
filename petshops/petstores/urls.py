from django.urls import path,include
from .views import LocationViewSet,PetstoreViewSet,CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'locations',LocationViewSet,basename='location')
router.register(r'petstores',PetstoreViewSet,basename='petstore')
router.register(r'categories',CategoryViewSet,basename='category')
urlpatterns = [
    path("",include(router.urls)),
]

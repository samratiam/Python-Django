from django.urls import path,include
from .views import LocationViewSet,PetstoreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'locations',LocationViewSet,basename='location')
router.register(r'petstores',PetstoreViewSet,basename='petstore')
urlpatterns = [
    path("",include(router.urls)),
]

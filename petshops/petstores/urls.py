from django.urls import path,include
from .views import LocationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'locations',LocationViewSet,basename='location')

urlpatterns = [
    path("",include(router.urls)),
]

from django.urls import path,include
from . import views
from .views import Create,List

urlpatterns = [
    # path("",views.post,name="posts")
    path("create/",Create.as_view(),name="create"),
    path("list/",List.as_view(),name="list"),
]


from django.urls import path, include
from rest_framework import routers

from beers import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'beers', views.BeerViewSet)
router.register(r'beer_types', views.BeerTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

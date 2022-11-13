from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .models import BeerType, Beer
from .serializers import UserSerializer, GroupSerializer, BeerSerializer, BeerTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BeerTypeViewSet(viewsets.ModelViewSet):
    queryset = BeerType.objects.all()
    serializer_class = BeerTypeSerializer
    permission_classes = [permissions.AllowAny]


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    permission_classes = [permissions.AllowAny]

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from beers.models import BeerType, Beer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BeerTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BeerType
        fields = ['name', 'description', ]


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = ['name', 'description', 'beer_type', ]

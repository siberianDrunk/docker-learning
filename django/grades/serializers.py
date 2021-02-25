from django.contrib.auth.models import User, Group
from .models import Grade, Direction
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class GradeSerializer(serializers.ModelSerializer):
    direction_id = serializers.PrimaryKeyRelatedField(source='Direction', queryset=Direction.objects.all())

    class Meta:
        model = Grade
        fields = ['id', 'title', 'img', 'desc', 'position', 'direction_id']


class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    grades = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Direction
        fields = ['id', 'title', 'importance', 'grades']

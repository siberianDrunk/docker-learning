from django.shortcuts import render
from .models import Grade, Direction
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, GradeSerializer, DirectionSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.


def index(request):
    grade = Grade.objects.all().order_by('position')
    directions = Direction.objects.all().order_by('importance')
    context = {'grade': grade, 'directions': directions}

    return render(request, 'index.html', context)


def apiIndex(request):
    print('API is working')

    return render(request, 'api.html')


def about(request):
    return render(request, 'about.html')




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GradesList(generics.ListCreateAPIView):
    queryset = Grade.objects.all().order_by('Direction__importance')
    serializer_class = GradeSerializer


class GradesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer



class DirectionList(generics.ListCreateAPIView):
    queryset = Direction.objects.all().order_by('importance')
    serializer_class = DirectionSerializer



from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer
# Create your views here.

# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.filter(user__is_active=True)
    serializer_class = TeacherSerializer
    http_method_names = ['get']

from django.shortcuts import render
from rest_framework import viewsets, permissions
from resources.models import Book
from resources.serializers import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
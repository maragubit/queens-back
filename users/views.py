from django.shortcuts import render

from users.models import User
from users.serializers import UserSimpleSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response

class UserSimpleViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSimpleSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]  # Allow only authenticated users
    
    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request, pk=None):
        user = self.request.user
        serializer = UserSimpleSerializer(user, context={'request': request})
        return Response(serializer.data)

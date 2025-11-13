from django.shortcuts import render
from rest_framework import viewsets, permissions
from students.permissions import IsOwnerOrReadOnly
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get','patch']
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    @action(detail=False, methods=['get'], url_path='me')
    def get_my_student(self,request):
        user = request.user
        try:
            student = Student.objects.filter(user=user).first()
            if not student:
                return Response({'detail': 'Student profile not found.'}, status=404)
            return Response(StudentSerializer(student, context={'request': request}).data)
        except Student.DoesNotExist:
            return Response({'detail': 'Student profile not found.'}, status=404)

from rest_framework import serializers

from courses.serializers import CourseSerializer
from .models import Audio, Book, Document

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['id', 'title', 'file', 'description', 'course']
        read_only_fields = fields
        
class BookSerializer(serializers.ModelSerializer):
    course=CourseSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'file', 'course']
        read_only_fields = fields
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'description', 'course']
        read_only_fields = fields
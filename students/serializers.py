from rest_framework import serializers
from courses.serializers import ClassroomSerializer
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    course=serializers.SerializerMethodField()
    classrooms = ClassroomSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['classrooms', 'course','classrooms']
        read_only_fields = fields

    def get_course(self, obj):
        return obj.get_course().title if obj.get_course() else None
from rest_framework import serializers
from courses.serializers import ClassroomSerializer
from .models import Student
from courses.models import Classroom


class StudentSerializer(serializers.ModelSerializer):
    course=serializers.SerializerMethodField()
    classrooms = ClassroomSerializer(many=True, read_only=True)
    classroom_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Classroom.objects.all(),
        source='classrooms',
        write_only=True
    )
    class Meta:
        model = Student
        fields = ['id','course','classrooms','classroom_ids']
        read_only_fields = ['id','course']
    def get_course(self, obj):
        return obj.get_course().title if obj.get_course() else None
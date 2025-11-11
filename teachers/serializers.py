from rest_framework import serializers

from users.serializers import UserVerySimpleSerializer
from .models import Teacher
from courses.serializers import ClassroomSerializer

class TeacherSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True, read_only=True)
    user = UserVerySimpleSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.fields]
    
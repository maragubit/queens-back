from rest_framework import serializers
from .models import User

class UserSimpleSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role','first_name','last_name', 'image','phone','birthdate']
        read_only_fields = fields
    
    def to_representation(self, instance):
        from teachers.serializers import TeacherSerializer
        from students.serializers import StudentSerializer

        representation = super().to_representation(instance)
        if hasattr(instance, 'teacher'):
            representation['teacher'] = TeacherSerializer(instance.teacher).data
        if hasattr(instance, 'student'):
            representation['student'] = StudentSerializer(instance.student).data
        return representation
    
class UserVerySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'image']
        read_only_fields = fields

from courses.models import Course, Classroom
from rest_framework import serializers



class ClassroomSerializer(serializers.ModelSerializer):

    teacher_name = serializers.SerializerMethodField()
    day_display = serializers.CharField(source='get_day_display', read_only=True)

    class Meta:
        model = Classroom
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.fields]
        
    def get_teacher_name(self, obj):
        return obj.teacher_name()
        
    
class CourseSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.fields]
    
        


    
from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    acronym = models.CharField(max_length=20)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    

days_list=[
    ('monday','lunes'),
    ('tuesday','martes'),
    ('wednesday','miércoles'),
    ('thursday','jueves'),
    ('friday','viernes'),
    ('saturday','sábado'),
    ('sunday','domingo'),
]    
class Classroom(models.Model):
    course = models.ForeignKey(Course, related_name='classrooms', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher', related_name='classrooms', on_delete=models.CASCADE)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    day = models.CharField(max_length=100, choices=days_list, blank=True, null=True)

    def __str__(self):
        return f'{self.course.title} {self.day}  {self.start_time} - {self.end_time} | {self.teacher.user.first_name}'
    
    def teacher_name(self):
        return f'{self.teacher.user.first_name} '
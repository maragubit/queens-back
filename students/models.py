from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField('users.User', related_name='student', on_delete=models.CASCADE)
    classrooms = models.ManyToManyField('courses.Classroom', blank=True, related_name='students')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def get_course(self):      
        classroom= self.classrooms.all().last()
        if classroom:
            return classroom.course
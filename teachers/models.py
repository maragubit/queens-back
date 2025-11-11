from django.db import models

# Create your models here.
class Teacher(models.Model):
    user=models.OneToOneField('users.User', related_name='teacher', on_delete=models.CASCADE)
    short_description=models.CharField(max_length=255, blank=True, null=True)
    
    
    
    def __str__(self):
        if self.user.gender == 'male':
            return f'Mr. {self.user.username}'
        elif self.user.gender == 'female':
            return f'Mrs. {self.user.username}'
        return f'Teacher: {self.user.username}'
    
    def save(self, *args, **kwargs):
        if self.user.role == 'teacher' or self.user.role == 'admin':
            super().save(*args, **kwargs)
        else:
            raise ValueError("Associated user must have role 'teacher' or 'admin'")
        
    def timetable(self):
        classrooms = self.classrooms.all()
        timetable = {}
        for classroom in classrooms:
            day = classroom.day
            timetable[day].append({
                'course': classroom.course.title,
                'start_time': classroom.start_time,
                'end_time': classroom.end_time
            })
        return timetable
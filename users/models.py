from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

role_list = [
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
]
gender_list=[
    ('male','Male'),
    ('female','Female'),
    ('other','Other'),
]
class User(AbstractUser):
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    gender=models.CharField(max_length=10, choices=gender_list, blank=True, default="female", null=True)
    role = models.CharField(max_length=50, choices=role_list, default='student')
    image=models.ImageField(upload_to='user_images/', blank=True, null=True)
    birthdate=models.DateField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk is None or not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        if self.email:
            self.username=self.email
        super().save(*args, **kwargs)
       
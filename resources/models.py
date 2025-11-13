from django.db import models

# Create your models here.

class Audio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='audios/')
    course=models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, related_name='audios')
    
    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    course=models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, related_name='books')
    file=models.FileField(upload_to='books/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='documents/')
    course=models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, related_name='documents')
    
    def __str__(self):
        return self.title
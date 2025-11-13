from django.contrib import admin
from .models import Audio, Book, Document

# Register your models here.
admin.site.register(Audio)
admin.site.register(Book)
admin.site.register(Document)
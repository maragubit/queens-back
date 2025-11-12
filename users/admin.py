from django.contrib import admin
from .models import User,EmailList
# Register your models here.
admin.site.site_header = "Queens English Institute – Panel de Administración"
admin.site.site_title = "Queens English Institute Admin"
admin.site.index_title = "Bienvenido al panel administrativo"
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'role', 'is_staff')
    list_filter = ('is_active', 'role')  # Optional: add filters on the right sidebar
    search_fields = ('username', 'email', 'first_name', 'last_name')        # Optional: add a search bar
    ordering = ('-date_joined',)             # Optional: default order
    list_editable = ('is_active', 'role')             # Optional: make fields editable directly from the list view
    
admin.site.register(EmailList)
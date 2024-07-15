from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_completed', 'date')
    list_filter = ('is_completed', 'date')
    search_fields = ('title', 'description')
    ordering = ('-date',)

admin.site.register(Task, TaskAdmin)
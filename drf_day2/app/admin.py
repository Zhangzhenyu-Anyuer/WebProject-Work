from django.contrib import admin

# Register your models here.
from app import models


@admin.register(models.Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ['name','age','gender']

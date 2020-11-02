from django.contrib import admin

# Register your models here.
from api import models


@admin.register(models.Book,models.Author,models.Press,models.Detail_Author)
class MyAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin

# Register your models here.
from user import models
# @admin.register(models.User)--> 相当与admin.site.register(models.User,UserAdmin)
# 并且这个装饰器支持多模型 @admin.register(models.User,models.XX,site=XXXX)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','gender']

admin.site.register(models.User,UserAdmin)
admin.site.site_header = 'zzy后台管理'

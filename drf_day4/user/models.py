from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=22,verbose_name='用户名')
    password = models.CharField(max_length=22,verbose_name='密码')
    details = models.OneToOneField(to='UserDetail',on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.username

class UserDetail(models.Model):
    address = models.CharField(max_length=22,verbose_name='地址',null=True)
    phone = models.CharField(max_length=22,verbose_name='手机号',null=True)
    head_pic = models.ImageField(upload_to='media/%Y/%m',default='media/1.jpg',verbose_name='用户头像')

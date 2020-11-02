from django.db import models

# Create your models here.
class Teacher(models.Model):
    gender_choices = (
        (0,'male'),
        (1,'female'),
        (2,'other'),
    )
    name = models.CharField(max_length=20,verbose_name='姓名')
    age = models.SmallIntegerField(verbose_name='年龄')
    password = models.CharField(max_length=20,verbose_name='密码')
    gender = models.SmallIntegerField(choices=gender_choices,default='0',verbose_name='性别')
    phone = models.CharField(max_length=20,null=True,blank=True,verbose_name='手机号')
    head_pic = models.ImageField(upload_to='pics/',default='pics/1.jpg',verbose_name='头像')
    subject = models.CharField(max_length=20,null=True,verbose_name='科目')
    class Meta:
        db_table = 't_Teacher'
        verbose_name = '教师表'
        verbose_name_plural = verbose_name
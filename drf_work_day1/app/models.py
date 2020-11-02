from django.db import models

# Create your models here.

class User(models.Model):
    gender_choices = (
        (0,'male'),
        (1,'female'),
        (2,'other'),
    )
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=gender_choices,default=0)
    class Meta:
        db_table = 'zz_user'
        verbose_name = '用户'

class User2(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, 'female'),
        (2, 'other'),
    )
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)

    class Meta:
        db_table = 'zz_user'
        verbose_name = '用户2'
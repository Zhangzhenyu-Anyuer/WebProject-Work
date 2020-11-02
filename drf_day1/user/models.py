from django.db import models

class User(models.Model):
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
        verbose_name = '用户'
        verbose_name_plural = verbose_name  # 可以将用户后面的s去掉
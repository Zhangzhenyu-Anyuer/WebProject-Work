# Generated by Django 2.0.6 on 2020-10-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, '男'), (1, '女'), (2, '未知')], default='0', verbose_name='性别'),
        ),
    ]
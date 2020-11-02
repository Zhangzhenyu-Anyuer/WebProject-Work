# Generated by Django 2.0.6 on 2020-10-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('gender', models.SmallIntegerField(choices=[(0, '男'), (1, '女'), (2, '未知')], default='男', verbose_name='性别')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号')),
                ('head_pic', models.ImageField(default='pics/1.jpg', upload_to='pics/', verbose_name='头像')),
                ('subject', models.CharField(max_length=20, null=True, verbose_name='科目')),
            ],
            options={
                'verbose_name': '教师表',
                'verbose_name_plural': '教师表',
                'db_table': 't_Teacher',
            },
        ),
    ]
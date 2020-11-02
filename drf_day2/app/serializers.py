from django.conf import settings
from rest_framework import serializers

from app.models import Teacher


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    phone = serializers.CharField()
    subject = serializers.CharField()

    gender = serializers.SerializerMethodField()
    def get_gender(self,obj):
        """
        自定义字段
        : self: 这是是序列器对象
        :param obj: 当前被序列化的对象
        :return:
        """
        return obj.get_gender_display() # 这里是指实现了choice的字段
    head_pic = serializers.SerializerMethodField()
    def get_head_pic(self,obj):
        return '%s%s%s' %('http://127.0.0.1:8000/',settings.MEDIA_URL,str(obj.head_pic))


class TeacherDeSerialize(serializers.Serializer):
    # 添加校验规则
    name = serializers.CharField(
        max_length=50,
        min_length=1,
        error_messages={
            'max_length': '姓名过长',
            'min_length': '姓名不能为空',
        }
    )
    password = serializers.CharField()
    age = serializers.IntegerField()
    phone = serializers.CharField()
    subject = serializers.CharField()

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
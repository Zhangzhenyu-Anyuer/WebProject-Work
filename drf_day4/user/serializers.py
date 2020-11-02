from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'username':{
                'required': True,
                'min_length': 3,
            },
            'password':{
                'required': True,
                'min_length': 3,
                'write_only': True
            },
            'details':{
                'write_only': True
            }
        }
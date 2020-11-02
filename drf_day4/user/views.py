from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def login(self,request,*args,**kwargs):
        request_data = request.data
        result = User.objects.filter(username=request_data.get('username'),password=request_data.get('password'))
        if result:
            return Response({
                'status': status.HTTP_200_OK,
                'message': '登录成功',
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': '登录失败'
        })

    def register(self,request,*args,**kwargs):
        request_data = request.data
        result = User.objects.filter(username=request_data.get('username'))
        if result:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '用户名已存在'
            })
        serializer = UserSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        save_obj = serializer.save()
        return Response({
            'status': 200,
            'message': '创建成功',
            'results': UserSerializer(save_obj).data
        })

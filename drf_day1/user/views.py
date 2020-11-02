from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from user.models import User

@csrf_exempt
def index(request):
    if request.method == 'GET':
        user_id = request.GET.get('id')
        try:
            objects_user = User.objects.get(pk=user_id)
            return JsonResponse({
                'status': 200,
                'message': '查询用户成功',
                'result': objects_user,
                })
        except:
            objects_user = User.objects.all().values('username','gender')
            return JsonResponse({
                'status': 200,
                'message': '查询所有用户成功',
                'result': list(objects_user)
            })
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        create_user = User.objects.create(username=username, password=pwd)
        print('POST 新增')
        return JsonResponse({
            'status': 200,
            'message': '新增用户成功',
            'result': create_user.username,
        })

@method_decorator(csrf_exempt,name='dispatch')
class UserView(View):
    def get(self,request,*args,**kwargs):
        user_id = kwargs.get('id')
        print(user_id)
        if user_id:
            objects_user = User.objects.get(pk=user_id).username
            return JsonResponse({
                'status': 200,
                'message': '查询用户成功',
                'result': objects_user,
            })
        else:
            objects_user = User.objects.all().values('username', 'gender')
            return JsonResponse({
                'status': 200,
                'message': '查询所有用户成功',
                'result': list(objects_user)
            })
    def post(self,request,*args,**kwargs):
        try:
            username = request.POST.get('username')
            pwd = request.POST.get('password')
            create_user = User.objects.create(username=username, password=pwd)
            print('POST 新增')
            return JsonResponse({
                'status': 200,
                'message': '新增用户成功',
                'result': create_user.username,
            })
        except:
            return JsonResponse({
                'status': 400,
                'message': '新增失败',
            })

    def delete(self,request,*args,**kwargs):
        user_id = kwargs.get('id')
        if user_id:
            print(user_id)
            objects_filter = User.objects.filter(pk=user_id)
            if objects_filter:
                objects_filter[0].delete()
                return JsonResponse({
                    'status': 200,
                    'message': '删除成功',
                })
        return JsonResponse({
            'status': 400,
            'message': '用户不存在,删除失败',
            })







class User_View(APIView):
    def get(self,request,*args,**kwargs):
        user_id = kwargs.get('id')
        print(user_id)
        if user_id:
            objects_user = User.objects.get(pk=user_id).username
            return JsonResponse({
                'status': 200,
                'message': '查询用户成功',
                'result': objects_user,
            })
        else:
            objects_user = User.objects.all().values('username', 'gender')
            return JsonResponse({
                'status': 200,
                'message': '查询所有用户成功',
                'result': list(objects_user)
            })

    def post(self,request,*args,**kwargs):
        try:
            username = request.POST.get('username')
            pwd = request.POST.get('password')
            create_user = User.objects.create(username=username, password=pwd)
            print('POST 新增')
            return JsonResponse({
                'status': 200,
                'message': '新增用户成功',
                'result': create_user.username,
            })
        except:
            return JsonResponse({
                'status': 400,
                'message': '新增失败',
            })
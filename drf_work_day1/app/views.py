from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.models import User

@csrf_exempt
def index(request):
    if request.method == 'GET':
        objects_all = User.objects.all()
        user_id = request.GET.get('id')
        return JsonResponse({
            'status': 200,
            'message': '查询用户成功',
            'result': objects_all.values(pk=user_id),
        })
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        User.objects.create(username=username,password=pwd)
        print('POST 新增')
        return JsonResponse({
            'status':200,
            'message': '新增用户成功',
            'result': '',
        })
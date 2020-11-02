from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer
from app.serializers import TeacherSerializer,TeacherDeSerialize
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from app.models import Teacher

class TeacherAPIView(APIView):
    # 局部使用渲染器
    # renderer_classes = [BrowsableAPIRenderer]

    # 局部使用解析器  代表的是局部只能接收json格式的数据
    # parser_classes = [JSONParser]
    # def get(self,request,*args,**kwargs):
    #     """
    #     get 方法中无法使用request.data 而使用request.query_params来接收参数
    #     """
    #     print("get Success")
    #     print(request._request.GET.get('name')) # _request是Request类
    #     print(request.GET.get('name'))
    #     print(request.query_params.get('name'))
    #
    #     return Response('GET OK')
    # def post(self,request,*args,**kwargs):
    #
    #     print('post Success')
    #     print(request._request.POST.get('name'))  # 前两个在接收参数的时候不能接收json格式的参数
    #     print(request.POST.get('name'))
    #     # request.data可以从前端获取多种类型的参数，兼容性强
    #     print(request.data)
    #     return Response('POST OK',status=200)

    def get(self,request,*args,**kwargs):
        t_id = kwargs.get('id')
        if t_id:
            t_obj = Teacher.objects.get(pk=t_id)
            t_serializer = TeacherSerializer(t_obj).data
            return Response({
                'status': 200,
                'message': '查询单个教师成功',
                'results': t_serializer,
            })
        else:
            teacher_objects_all = Teacher.objects.all()
            return_dict = TeacherSerializer(teacher_objects_all, many=True).data
            return Response({
                'status': 200,
                'message': '查询所有教师成功',
                'results': return_dict,
            })

    def post(self,request,*args,**kwargs):
        request_data = request.data
        print(request_data)
        if not isinstance(request_data,dict) or request_data == {}:
            return Response({
                'status': 400,
                'message': '参数有误',
            })
        else:
            teacher_serializer = TeacherDeSerialize(data=request_data)
            # print(teacher_serializer)
            if teacher_serializer.is_valid():
                teacher_save = teacher_serializer.save()
                print(teacher_save)
                return Response({
                    'status': 200,
                    'message': '添加教师成功',
                    'result': TeacherSerializer(teacher_save).data,
                })
            else:
                return Response({
                    'status': 400,
                    'message': '出错',
                    'result': teacher_serializer.errors
                })
    def delete(self,request,*args,**kwargs):
        get_id = request.data.get('id')
        if get_id:
            get_Queryset = Teacher.objects.filter(pk=get_id)
            if get_Queryset:
                get_Queryset.delete()
                return Response({
                    'status': 200,
                    'message': '删除单个成功',
                })
        return Response({
            'status': 400,
            'message': '删除失败',
        })
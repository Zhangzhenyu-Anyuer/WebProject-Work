from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from api.models import Book
from api.serializers import BookModelSerializer, BookListSerializer, BookModelSerializerV2
from rest_framework import mixins

class BookAPIView(APIView):
    def get(self,request,*args,**kwargs):
        book_id = kwargs.get('id')
        if book_id:
            book_obj = Book.objects.get(pk=book_id)
            serializer = BookModelSerializer(book_obj).data
            return Response({
                'status': 200,
                'message': '查询单个对象成功',
                'results': serializer,
            })
        else:
            all_obj = Book.objects.all()
            all_serializer = BookModelSerializer(all_obj,many=True).data
            return Response({
                'status': 200,
                'message': '查询所有对象成功',
                'results': all_serializer,
            })

    def post(self,request,*args,**kwargs):
        request_data = request.data
        if isinstance(request_data,dict):
            many = False
        elif isinstance(request_data,list):
            many = True
        else:
            return Response({
                'status': 400,
                'message': '参数有误',
            })
        print(request_data)
        serializer = BookModelSerializer(data=request_data, many=many)
        serializer.is_valid(raise_exception=True)
        book_obj = serializer.save()
        return Response({
            'status': 200,
            'message': '新增成功',
            'results': BookModelSerializer(book_obj,many=many).data
        })

    def delete(self,request,*args,**kwargs):
        book_id = kwargs.get('id')
        if book_id:
            # 删除单个
            ids = [book_id]
        else:
            # 删除多个
            ids = request.data.get('ids')
        queryset_objs = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        if queryset_objs:
            return Response({
                'status': 200,
                'message': '删除成功',
            })
        else:
            return Response({
                'status': 400,
                'message': '删除失败',
            })

    # def put(self,request,*args,**kwargs):
    #     """
    #     整体修改单个
    #     """
    #     request_data = request.data
    #     book_id = kwargs.get('id')
    #     try:
    #         book_obj = Book.objects.get(pk=book_id)
    #     except:
    #         return Response({
    #             'status': 400,
    #             'message': '图书不存在',
    #         })
    #     serializer = BookModelSerializer(data=request_data, instance=book_obj)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({
    #         'status': 200,
    #         'message': '修改成功',
    #         'results': BookModelSerializer(book_obj).data
    #     })
    # def patch(self,request,*args,**kwargs):
    #     """
    #     更新单个局部
    #     """
    #     request_data = request.data
    #     book_id = kwargs.get('id')
    #     try:
    #         book_obj = Book.objects.get(pk=book_id)
    #     except:
    #         return Response({
    #             'status': 400,
    #             'message': '图书不存在',
    #         })
    #
    #     serializer = BookModelSerializer(data=request_data, instance=book_obj)
    #     print(serializer)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({
    #         'status': 200,
    #         'message': '修改成功',
    #         'results': BookModelSerializer(book_obj).data
    #     })

    def patch(self,request,*args,**kwargs):
        book_id = kwargs.get('id')
        request_data = request.data
        if book_id: # 修改单个
            book_list = [book_id]
            book_objs = [request_data]
        elif not book_id and isinstance(request_data,list): # 修改多个
            book_list=[]
            book_objs = []
            for index,i in enumerate(request_data):
                id = i.pop('id')
                try:
                    books = Book.objects.get(pk=id)
                    book_list.append(books)
                    book_objs.append(request_data[index])
                except Book.DoesNotExist:
                    continue
        else:
            return Response({
                'status': 400,
                'message': '参数有误'
            })
        model_serializer = BookModelSerializerV2(data=book_objs, instance=book_list, many=True, partial=True)
        model_serializer.is_valid(raise_exception=True)
        model_serializer.save()
        return Response({
            'status': 200,
            'message': 'ok'
        })


class BookGenericAPIView(generics.GenericAPIView,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializerV2
    lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
        # book_list = self.get_queryset()
        # print(book_list)
        # serializer = self.get_serializer(book_list,many=True).data
        # print(serializer)
        # return Response({
        #     'status': 200,
        #     'message': '查询成功',
        #     'results': serializer
        # })
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class BookViewSet(viewsets.ViewSet):
    queryset = None
    serializer_class = None
    lookup_field = 'pk'
    def login(self,request):
        return Response('OK')
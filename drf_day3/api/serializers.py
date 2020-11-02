from rest_framework import serializers

from api.models import Book, Press, Author


class PressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ('press_name', 'address')


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_name']


class BookListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        for index,obj in enumerate(instance):
            self.child.update(obj,validated_data[index])
        print(instance)
        return instance

class BookModelSerializer(serializers.ModelSerializer):
    # publish = PressModelSerializer()
    # author = AuthorModelSerializer(many=True)
    class Meta:
        model = Book
        fields = ('book_name', 'price', 'publish', 'author', 'pic')
        read_only_fields = ['pic']

        list_serializer_class = BookListSerializer

        extra_kwargs = {
            'book_name': {
                'required': True,
                'min_length': 1,
                'error_messages': {
                    'required': '图书名必须提供',
                    'min_length': '图书名不能为空'
                }
            },
            'pic': {
                # read_only 指的是某个字段只参加序列化
                'read_only': True
            },
            'publish':{
                # write_only 指的是字段只参加反序列化
                'write_only': True
            },
            'author': {
                'write_only': True
            }
        }
    # def validate(self, attrs):
        # publish = attrs.get('publish')
        # serializer = PressModelSerializer(publish)
        # attrs['publish'] = serializer
        # return attrs

    # def validate_book_name(self,obj):
    #     print(obj)
    #     return obj

class BookModelSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_name','price', 'publish', 'author', 'pic']
        read_only_fileds = ['pic']

        list_serializer_class = BookListSerializer

        extra_kwargs = {
            'book_name': {
                'required': True,
                'min_length': 1,
                'error_messages': {
                    'required': '图书名必须提供',
                    'min_length': '图书名不能为空'
                }
            },
            'publish': {
                'write_only': True
            },
            'author': {
                'write_only': True
            }

        }
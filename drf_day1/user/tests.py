from django.test import TestCase

# Create your tests here.

def add(*args,**kwargs):
    print(*args)  # 输出的是原格式
    print(args)  # 输出的是元组类型
    print(kwargs) # 输出的是字典格式
    print(type(kwargs))

add([1,2,3],a=1,d=3)
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        # 可以继承该表中的字段
        abstract = True


class Book(BaseModel):
    book_name = models.CharField(max_length=22, verbose_name='书名')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='价格')
    pic = models.ImageField(upload_to='pics/', default='pics/1.jpg', verbose_name='图片')
    publish = models.ForeignKey(to='Press', on_delete=models.CASCADE, db_constraint=False, related_name='books')
    author = models.ManyToManyField(to='Author', db_constraint=False, related_name='books')

    class Meta:
        db_table = 't_book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name

class Author(BaseModel):
    author_name = models.CharField(max_length=22, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')

    class Meta:
        db_table = 't_author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author_name


class Press(BaseModel):
    press_name = models.CharField(max_length=22, verbose_name='出版社')
    address = models.CharField(max_length=22, verbose_name='地址')

    class Meta:
        db_table = 't_press'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.press_name


class Detail_Author(BaseModel):
    mobile = models.CharField(max_length=22, verbose_name='手机号')
    address = models.CharField(max_length=22, verbose_name='地址')
    author = models.OneToOneField(to='Author', on_delete=models.CASCADE, related_name='detail_author')

    class Meta:
        db_table = 't_detail_author'
        verbose_name = '作者详情'
        verbose_name_plural = verbose_name

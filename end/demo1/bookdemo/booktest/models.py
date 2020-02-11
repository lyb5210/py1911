from django.db import models

# Create your models here.
# MVT M数据模型
# ORM M数据模型
# 在此处编写应用的模型类
# 每一张表就是一个模型类
# 通过模型类操作数据库
#1 注册模型 在setting.py中的INSTALLED_APPS 添加应用名
# 2 生成迁移文件 用于数据库交互 python manage.py makemigrations
# 3 执行迁移 python manage.py migrate
class Book(models.Model):
    """
    book继承了Model类 成为Model类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")

class Hero(models.Model):
    """

    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','nv')),default='male')
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
from django.db import models


# Create your models here.

class Userinfo(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, null=True)
    pwd = models.CharField(max_length=32, null=True)
    age = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=32, null=True)
    country = models.CharField(max_length=32, null=True)
    fullname = models.CharField(max_length=32, null=True)

    # def __str__(self):
    #     return f'数据对象{self.username}'


class Books(models.Model):
    title = models.CharField(max_length=32)

    price = models.DecimalField(max_digits=8, decimal_places=2)
    # max_digits=8,decimal_places=2 两个参数的意思时总共八位数，支持小数两位

    creat_time = models.DateField(auto_now_add=True)

    # auto_now=True,auto_now_add=True 两个参数只自动更新时间，只在数据创建的时候创建时添加时间
    def __str__(self):
        return self.title

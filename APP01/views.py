from django.shortcuts import render, HttpResponse, reverse, redirect
from APP01 import models  # 导入models
from django.http import JsonResponse
import os
from django.views import View
# Create your views here.


class Mylogin(View):  # 继承View类
    # def up(self, request):
    #     return render(request, 'up.html')

    def get(self, request):
        return HttpResponse('GET')

    def post(self, request):
        return HttpResponse('POST')


def json(request):
    a = [11, 22, 33, 44, 55]
    return JsonResponse(a, safe=False)


# 前端上传文件到本地
def up_file(request):
    file = request.FILES.get('my_file')
    file_type = os.path.splitext(file.name)[1]  # 获取上传文件类型
    with open(f'a{file_type}', 'wb') as f:  # 根据文件格式自动创建该格式文件
        for line in file:
            f.write(line)
    return render(request, 'up_file.html')


# 登录
def login(request):
    return render(request, 'login.html')


def index(request):
    # """ 获取前端提交数据 """
    username = request.POST.get('username', )
    password = request.POST.get('password', )
    print(username, password)
    # """ 获取数据库数据 """
    user_obj = models.Userinfo. \
        objects.filter(username=username)[0]
    if user_obj.pwd == password:
        return render(request, 'login_success.html')
    else:
        return render(request, 'login_failed.html')


# 注册
def register(request):
    # 获取前端注册信息
    username = request.POST.get('username')
    password = request.POST.get('password')
    fullname = request.POST.get('fullname')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    country = request.POST.get('country')

    # 第一种写入方式
    models.Userinfo.objects.create(username=username,
                                   pwd=password,
                                   fullname=fullname,
                                   age=age,
                                   gender=gender,
                                   country=country
                                   )

    # 第二种写入方式
    # obj = models.Userinfo()
    # obj.name = username
    # obj.pwd = password
    # obj.save()

    return render(request, 'register.html')


#基本信息
def ser(request):
    data = models.Userinfo.objects.all()
    return render(request, 'ser.html', locals())


# 编辑
def edit(request):
    uid = request.GET.get('uid')
    edit_obj = models.Userinfo. \
        objects.filter(uid=uid).first()
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        country = request.POST.get('country')
        models.Userinfo.objects. \
            filter(uid=uid).update(fullname=fullname,
                                   gender=gender,
                                   age=age,
                                   country=country)
        return redirect('/APP01/ser/')
    return render(request, 'edit.html', locals())


# 删除
def dele(request):  # 删除信息
    uid = request.GET.get('uid')
    models.Userinfo.objects. \
        filter(uid=uid).delete()
    return redirect('/APP01/ser/')


# 查看详细信息
def userinfo(request):
    uid = request.GET.get('uid')
    data = models.Userinfo. \
        objects.filter(pk=uid).all()
    return render(request, 'userinfo.html', locals())

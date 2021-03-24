from APP01 import views
from django.urls import path

urlpatterns = [
    # 登录接口
    path('index/', views.index),
    path('login/', views.login),
    # 注册接口
    path('register/', views.register),
    # 查询接口
    path('ser/', views.ser),
    # 编辑接口
    path('edit/', views.edit),
    # 删除接口
    path('dele/', views.dele),
    # 用户信息接口
    path('userinfo/', views.userinfo),
    # 文件上传接口
    path('upfile/', views.up_file),

    path('json/', views.json),

    path('upa/', views.Mylogin.as_view())

]

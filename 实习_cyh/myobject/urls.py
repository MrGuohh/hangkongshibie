"""myobject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from web.views import index
from django.urls import path,include

urlpatterns = [
    path('', include("web.urls")),                # 默认前台端
    path('myadmin/', include("myadmin.urls")),     # 后台管理端
    path('web/', include("web.urls")),
    # path('login',index.login,name="web_login"),#加载登录表单
    # path('dologin',index.dologin,name="web_dologin"),#执行登录
    # path('logout',index.logout,name="web_logout"),#退出
    #path('verify',index.verify,name="web_verify"),#输出验证码
]

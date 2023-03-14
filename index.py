#后台视图
from django.shortcuts import render
from django.http import HttpResponse,FileResponse,JsonResponse

from django.shortcuts import redirect
from django.urls import reverse

from django.http import JsonResponse

import pandas as pd
# import numpy as pd
import os

#后台首页
def index(request):
    return render(request,'myadmin/login.html')

def login(request):
    return render(request,'myadmin/login.html')

# 会员执行登录
def dologin(request):
    try:
        #根据登录账号获取用户信息
        adnumber=request.POST['adnumber']
        passnumber=request.POST['passnumber']
        adminuser=0
        # 校验当前用户状态是否是管理员
        if adnumber == "123456" and passnumber=="123":
                # 将当前登录成功用户信息以adminuser这个key放入到session中
            adminuser=1
            return redirect(reverse('myadmin_index'))
        else:
            context={"info":"此用户非后台管理账号！"}
    except Exception as err:
        print(err)
        context={"info":"登录账号不存在！"}
    return render(request,"myadmin/index.html",context)

# 退出登录
def logout(request):
    return redirect(reverse('myadmin_login'))


def upload(request):
    # if request.method == 'POST' :
    #     # 获取上传的文件
    #     # and request.FILES['myfile']
    #     # myfile = request.FILES['myfile']

    #     # # 使用 Pandas 读取 CSV 文件
    #     # df = pd.read_csv(myfile)

    #     # 进行相应的处理
        
    #     # 返回处理结果
    #     return HttpResponse('处理成功')
    return render(request, "myadmin/upload.html")

def download(request):
    # 文件路径
    # file_path = '/path/to/processed_file.csv'

    # # 检查文件是否存在
    # if not os.path.exists(file_path):
    #     return HttpResponse('文件不存在') 

    # # 返回文件
    # return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='processed_file.csv')
    return HttpResponse('文件下载成功')


def dealwith(request):
    csv=pd.read_csv('myadmin/views/result.csv',encoding='utf-8')
    list0=['name','sign','posibility']
    list1=list(csv["pax_name"])
    list2=list(csv["emd_lable2"])
    list3=list(csv["probability"])
    # if request.method == 'POST':
    #     # 获取上传的文件
    #     # myfile = request.FILES['myfile']

    #     # # 使用 Pandas 读取 CSV 文件
    #     # df = pd.read_csv(myfile)

    #     # 进行相应的处理,
        
    #     # 返回处理结果
    #      return HttpResponse('文件不存在')
    # else:  
    data=[{'name':a,"sign":b,"probability":c}for a,b,c in zip(list1,list2,list3)]
    return JsonResponse({"data":data})
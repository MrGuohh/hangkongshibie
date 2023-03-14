from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

#前台首页
def index(request):
    '''购票系统首页'''
    return render(request,'web/index.html')


def login(request):
    '''加载登录页面'''
    return render(request,'web/login.html')

def dologin(request):
    try:
        #根据登录账号获取用户信息
        telenumber=request.POST['telenumber']
        password=request.POST['password']
        adminuser=0
        # 校验当前用户状态
        if telenumber == "123456" and password=="123":
                # 将当前登录成功用户信息以adminuser这个key放入到session中
            adminuser=1
            return redirect(reverse('web_index'))
        else:
            context={"info":"此用户非后台管理账号！"}
    except Exception as err:
        print(err)
        context={"info":"登录账号不存在！"}
    return render(request,"web/index.html",context)

def logout(request):
    '''加载系统退出操作'''
    return redirect(reverse('web_login'))

def insheet(request):
    '''加载主页'''
    return render(request,'web/psheet.html')

def inbuy(request):
    '''加载购票'''
    return render(request,'web/buy.html')

def inorder(request):
    '''加载订单'''
    return render(request,'web/order.html')

def modify(request):
    '''修改信息'''
    return render(request,'web/modify.html')

def sheetout(request):
    '''加载系统退出操作'''
    return redirect(reverse('web_index'))

# def verify(request):
#     #引入随机函数模块
#     import random
#     from PIL import Image, ImageDraw, ImageFont
#     #定义变量，用于画面的背景色、宽、高
#     #bgcolor = (random.randrange(20, 100), random.randrange(
#     #    20, 100),100)
#     bgcolor = (242,164,247)
#     width = 100
#     height = 25
#     #创建画面对象
#     im = Image.new('RGB', (width, height), bgcolor)
#     #创建画笔对象
#     draw = ImageDraw.Draw(im)
#     #调用画笔的point()函数绘制噪点
#     for i in range(0, 100):
#         xy = (random.randrange(0, width), random.randrange(0, height))
#         fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
#         draw.point(xy, fill=fill)
#     #定义验证码的备选值
#     #str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
#     str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
#     #随机选取4个值作为验证码
#     rand_str = ''
#     for i in range(0, 4):
#         rand_str += str1[random.randrange(0, len(str1))]
#     #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
#     font = ImageFont.truetype('static/arial.ttf', 21)
#     #font = ImageFont.load_default().font
#     #构造字体颜色
#     fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
#     #绘制4个字
#     draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
#     draw.text((25, -3), rand_str[1], font=font, fill=fontcolor)
#     draw.text((50, -3), rand_str[2], font=font, fill=fontcolor)
#     draw.text((75, -3), rand_str[3], font=font, fill=fontcolor)
#     #释放画笔
#     del draw
#     #存入session，用于做进一步验证
#     request.session['verifycode'] = rand_str
#     """
#     python2的为
#     # 内存文件操作
#     import cStringIO
#     buf = cStringIO.StringIO()
#     """
#     # 内存文件操作-->此方法为python3的
#     import io
#     buf = io.BytesIO()
#     #将图片保存在内存中，文件类型为png
#     im.save(buf, 'png')
#     #将内存中的图片数据返回给客户端，MIME类型为图片png
#     return HttpResponse(buf.getvalue(), 'image/png')
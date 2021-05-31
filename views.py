from django.shortcuts import render,redirect
#from django.shortcuts import render,redirect

# Create your views here.
from django.http import  HttpResponse#引入HttpResponse
from .models import Student,Grades
from datetime import  *

# def studentlist(request):
#     studentList=Student.objects.all()
#     return render(request,'myapp/StudentList.html',{"Studentttt":studentList})

# def gradeslist(request):
#     gradesList=Grades.objects.all()
#     return render(request,'myapp/gradesinfo.html',{"gradesinfo":gradesList})
#
# def studentlist(request,num):
#     # studentList=Student.objects.all()
#     gradesnum=Grades.objects.get(pk=num)
#     studentlists=gradesnum.student_set.all()
#     return render(request,'myapp/StudentList.html',{"Studentttt":studentlists})
#
#
#
# def showmain(request):
#     return render(request,'myapp/fileinput.html')
#
#
#
# def  Get_img(request):
#     getimg=Grades.gra.all()
#     stuimg=Student.stuobj.all()
#     return render(request,'myapp/show_pic.html',{"get_img":getimg,"get_stu":stuimg})
#
# def showfile(request):
#     return render(request,"myapp/show_pic.html")
#     pass
#
#
# def addGrades(request):
#     ffile=request.POST.get("file")
#     fimg=request.POST.get("img")
#
#     stu=Grades.createGrades("会计学",datetime(year=2020,month=12,day=11),
#                             22,ffile,fimg,)
#     stu.save()
#     return HttpResponse("提交成功")

# def showfile(request):
#     return render(request,"myapp/putfile.html")



def jjiang(request):

    return render(request, "myapp/aa.html")

def recive_jjiang(request):
    print(request.POST.get("name"))
    alist = request.POST.getlist("hh")
    print("alist: {}".format(alist))
    return HttpResponse("is ok")



import  os
from myapp.models import  PutFile

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def putfile(request):
    if request.method =="POST":
          myfile=request.FILES.get("file",None)
          if not myfile:
                return  HttpResponse("没有成功上传文件")
          destination=open(os.path.join("G:\\allpython\\django\\project\\media\\file",myfile.name),'wb+')
          #至少存进来了

          for chunk in myfile.chunks():
              destination.write(chunk)
          destination.close()

          putt=PutFile()
          putt.ffile=myfile
          putt.ffilename=myfile.name
          putt.save()
          return redirect('/getputimg/')


def getputimg(request):
    getimg1=Share.objects.all()
    print(getimg1[0].ffile.path)
    print(getimg1[0].ffile.name)
    print(getimg1[0].ffilename)


    return  render(request,'myapp/showputimg.html' ,{"imgg":getimg1})
from myapp.models import Share,User,ImgFile
from django.utils.encoding import escape_uri_path
from django.http import StreamingHttpResponse
def file_down(request,num):
    # getimg1 = Share.objects.get(pk=num)
    getimg1=ImgFile.objects.get(pk=num)
    imgpath=getimg1.iimg.path
    imgname=getimg1.iimgname

    # file=open("G:\\allpython\\django\\project\\media\\file\\QQ浏览器截图20200321112417_L6jziXh.png",'rb')
    file=open(imgpath,'rb')
    # response =StreamingHttpResponse(file)
    # response['Content-Type']='application/octet-stream'
    # response['Content-Disposition']='attachment;filename="{0}"'.format("jiangyuan.png")
    response =StreamingHttpResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']="attachment; filename*=utf-8''{}".format(escape_uri_path(imgname))

    return response

from .forms import GoodsForm

def getsorlimg(request):
    filee=PutFile.objects.get(id=6)
    return  render(request,'myapp/sorlthumntest.html',{"imgg":filee})
def showmaxpost(request):

    if request.session.get('username')==None:
        print(request.session.get('username'))
        return redirect('/main/')
    else:
        forms=GoodsForm()
        return  render(request,'myapp/edit_share.html',{"fromss":forms})


from itertools import *
from celeryTest.sms.tasks import  filestore,send_email
from re import  split
######往数据库存数据
def maxpost(request):
    userid=request.session.get("username",default="none")
    if  userid == "none":
        return redirect('/main/')

    else:
        wang=User.objects.get(username=userid)

        titles=request.POST.get("title")
        keywords=request.POST.get("keyword")
        dates=request.POST.getlist("dates")
        dateslist=dates[0].split("-")

        contents=request.POST.get("content")
        print(titles)
        print(keywords)


        if request.method =="POST":
              # myfile=request.FILES.get("files",None)
              # myimg=request.FILES.get("imgs",None)
              myfiles=request.FILES.getlist("files",None)
              myimgs=request.FILES.getlist("imgs",None)
              #
              # filestore.delay(myfiles,"G:\\allpython\\django\\project\\media\\file")
              # filestore.delay(myimgs,"G:\\allpython\\django\\project\\media\\iimg\\picture")


              # if not myfile:
              #       return  HttpResponse("没有成功上传文件")
              ###


              #至少存进来了
              for myfile in myfiles:
                  destination_file = open(os.path.join("G:\\allpython\\django\\project\\media\\file", myfile.name), 'wb+')
                  for chunk in myfile.chunks():
                      destination_file.write(chunk)
                  destination_file.close()
              for myimg in myimgs:
                  destination_img = open(os.path.join("G:\\allpython\\django\\project\\media\\iimg\\picture", myimg.name), 'wb+')
                  for chunk in myimg.chunks():
                      destination_img.write(chunk)
                  destination_img.close()

              sha=Share()



              sha.name="jiangyuan"
              sha.title=titles
              sha.keyword=keywords

              # sha.ffile=myfile
              # sha.ffilename=myfile.name
              # sha.iimg=myimg
              # sha.iimgname=myimg.name
              sha.datee=datetime(year=int(dateslist[0]),month=int(dateslist[1]),day=int(dateslist[2]))
              sha.content=contents

              sha.Touser=wang
              sha.save()
              for i in zip_longest(myfiles,myimgs):
                  if None in i:
                      return HttpResponse("有空欸")
                  else:
                      ImgFile.objects.create(ffile=i[0],ffilename=i[0].name,ffiletime=datetime(2020,1,11),iimg=i[1],iimgname=i[1].name,iimgtime=datetime(2020,1,11),Toblog=sha)
              # for i in zip(myfiles,myimgs):
              #     ImgFile.objects.create(ffile=i[0],ffilename=i[0].name,ffiletime=datetime(2020,11,1),iimg=i[1],iimgname=i[].name,iimgtime=datetime(2020,11,1,),Toblog_id=sha)








        return  redirect("/showshare/")




##########关于单个文件的上传
# def simpleput(request):
#     if request.POST.get("files"):
#         ##
#         myfiles=request.FILES.getlist("files",None)
#
#         # for myfile in myfiles:
#         #     destination_file = open(os.path.join("G:\\allpython\\django\\project\\media\\file", myfile.name), 'wb+')
#         #     for chunk in myfile.chunks():
#         #         destination_file.write(chunk)
#         #     destination_file.close()
#     # else:
#     #     ##
#     #     myimgs = request.FILES.getlist("imgs", None)
#     #     for myfile in myimgs:
#     #         destination_file = open(os.path.join("G:\\allpython\\django\\project\\media\\file", myfile.name), 'wb+')
#     #         for chunk in myfile.chunks():
#     #             destination_file.write(chunk)
#     #         destination_file.close()
#     return redirect("/showshare/")


#
#
#  ####显示所有条的详细信息
#
#
def showshare(request):
    if request.session.get("username",default="none") == "none":
        return redirect("/main/")
    else:

        sha=Share.objects.all()
        username=request.session.get("username")
        # sessionids=request.COOKIES['sessionid']
        #
        # print(request.session.get(sessionids))
        # print( list(request.session.keys())[1])
        # print("#########")
        # print(request.session.keys())
        # print(request.session.session_key)
        return  render(request,'myapp/showshare1.html',{"all":sha,'user':username})

def alinefile(request):
    sha=Share.objects.all()
    return  render(request,'myapp/alinefile.html',{"all":sha})

#
#
# ##编辑页面
#

def show_editpage(request,num):
    username=request.session.get("username")
    detail_share=Share.objects.get(pk=num)
    formss=GoodsForm(instance=Share.objects.get(pk=num))
    return render(request,'myapp/show_edit.html',{"first_one":detail_share,"second_one":formss,'username':username})


#登录界面

def main(request):

    return render(request, 'myapp/main.html')
    # return render(request,'myapp/main.html')

#######接收登录的验证消息
def put1(request):
    username = request.POST.get("username")
    pwd1 = User.objects.get(username=username).password

    pwd = request.POST.get("pwd")

    print(pwd1,pwd)
    if pwd1==pwd:
        request.session['username'] = username
        # request.session[username] = pwd
        return redirect("/showshare/")
    else:
        return HttpResponse("您输入的密码不正确")

#######注册界面
def user_register(request):

    return render(request,'myapp/user_register.html')



########接收注册而来的数据
def put(request):
    username = request.POST.get("username")
    pwd=request.POST.get('pwd')
    newuser=User()
    newuser.username=username
    newuser.password=pwd
    newuser.userauth=1
    newuser.save()

    # request.session.set_expiry(0)
    return  redirect('/main/')
#########登录后的界面
def login(request):

    return render(request,'myapp/login.html')

##########删除按钮

def delete_obj(request,num):
    Share.objects.get(pk=num).delete()

    return redirect("/showshare/")






from django.db.models import Q
from datetime import datetime
#############search功能的实现
def search_keyword(request):
    keywords=request.POST.get("keywords")
    starttime=request.POST.get("starttime")
    endtime=request.POST.get("endtime")
    starttime_list=starttime.split("-")
    endtime_list=endtime.split("-")

    # print(starttime[0].splits("-"))
    # print(endtime[0].splits("-"))
    # for i in starttime_list:
    #     if i:
    #         int(i)
    #     else:
    #         i=None


    sha=Share.objects.filter(Q(title__contains=keywords)|Q(keyword__contains=keywords)|Q(keyword__contains=keywords))
    # sha=Share.objects.filter(Q(datee__lte=datetime(year=int(endtime_list[0]),month=int(endtime_list[1]),day=int(endtime_list[2])))&Q(datee__gte=datetime(year=int(starttime_list[0]),month=int(starttime_list[1]),day=int(starttime_list[2]))))

    return  render(request,'myapp/showshare1.html',{"all":sha})

########根据日期来search
def search_date(request):
    print(request.POST)
    return  redirect("/showshare/")



####测试登录界面
# def login(request):
#     # if request.session:
#     #     print(request.session['jiang'])
#     #     print(request.session)
#     # else:
#     #     print("没有session的值")
#
#     return render(request,'myapp/login.html')
# def put(request):
#     username = request.POST.get("username")
#     request.session['jiang'] = username
#     request.session.set_expiry(60)
#     return  redirect('/main/')
# def main(request):
#     print(request.session)
#     print(request.POST)
#     username=request.session.get('jiang',default="游客")
#     # return render(request,'myapp/main.html')
#     return render(request,'myapp/main.html',{'username':username})
from django.contrib.auth import  logout
def quit(request):
    logout(request)
    return redirect('/main/')



######关于文件的下载
# def down(request,num):
#     sha=Share.objects.get(pk=num)
#     imgpath=sha.iimg.path
#     imgname=sha.iimgname
#
#     file=open(imgpath,'rb')
#     reponse=StreamingHttpResponse(file)
#     reponse['Content-type']='application/octet-stream'
#     reponse['Content-Disposition']="attachment;filename*=utf-8''{}".format(escape_uri_path(imgname))
#
#     return reponse

def down(request,num):
    # getimg1 = Share.objects.get(pk=num)
    getimg1 = ImgFile.objects.get(pk=num)

    imgpath=getimg1.iimg.path
    imgname=getimg1.iimgname

    # file=open("G:\\allpython\\django\\project\\media\\file\\QQ浏览器截图20200321112417_L6jziXh.png",'rb')
    file=open(imgpath,'rb')
    # response =StreamingHttpResponse(file)
    # response['Content-Type']='application/octet-stream'
    # response['Content-Disposition']='attachment;filename="{0}"'.format("jiangyuan.png")
    response =StreamingHttpResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']="attachment; filename*=utf-8''{}".format(escape_uri_path(imgname))

    return response



#######
####关于多个文件的上传操作
#####
def mulifile(request):
    # print(request.FILES.getlist("file",None))
    # obj=request.FILES.getlist("file",None)
    # print(request.FILES.getlist("file",None))


    # for i in obj:
    #     for chunk in i.chunks():
    #         destination_file = open(os.path.join("G:\\allpython\\django\\project\\media\\file", i.name), 'wb+')
    #         destination_file.write(chunk)
    #         destination_file.close()

    return render(request,'myapp/mulifile.html')

def collect_file(request):
    if request.method == "POST":
        myfiles = request.FILES.getlist("file", None)
        # print("{myfiles:}{myfiles111:>7}".format(myfiles,myfiles[0]))
        print(myfiles[0])
        return HttpResponse("ok")
        # myimg = request.FILES.get("imgs", None)

        # if not myfile:
        #       return  HttpResponse("没有成功上传文件")

        # for myfile in myfiles:
        #
        #
        #
        #     destination_file = open(os.path.join("G:\\allpython\\django\\project\\media\\file", myfile.name), 'wb+')
        #     # destination_img = open(os.path.join("G:\\allpython\\django\\project\\media\\iimg\\picture", myimg.name), 'wb+')
        #     # 至少存进来了
        #
        #     for chunk in myfile.chunks():
        #         destination_file.write(chunk)
        #     destination_file.close()

        # return redirect("/mulifile/")
        # for chunk in myimg.chunks():
        #     destination_img.write(chunk)
        # destination_img.close()
        #



  # if request.method=="POST":
  #   # obj1 = request.FILES.getlist("file", None)[0]
  #   # obj1 = request.FILES.getlist("file", None)
  #   obj1 = request.FILES.get("file",None)
  #   print(obj1)
  #   print(type(obj1))
  #   destination_file=open(os.path.join("G:\\allpython\\django\\project\\media\\file", obj1.name), 'wb+')
  #   for chunk in obj1.chunks:############chunks是有括号的，你妹的
  #       destination_file.write(chunk)
  #   destination_file.close()










########看视频之后的测试

###测试文件上传的问题
def upfile(request):
    return render(request,'myapp/django_static.html')

####测试page页面
from django.core.paginator import  Paginator

def showpage(request,pageid):
    alllist=Share.objects.all()

    paginator=Paginator(list(alllist),2)
    # print("{:>3}{:>3}{:>3}".format(paginator.count,paginator.num_pages,paginator.page_range))
    print("paginator_count", paginator.count,paginator.num_pages,paginator.page_range)
    ####把全部的数据分成每页两个
    pagedata=paginator.page(pageid)
    print()
    print("pagedata:",pagedata.object_list,pagedata.number,pagedata.paginator.page_range)
    print("pagedata.has_other_pages:",pagedata.has_other_pages())
    print("",pagedata.has_next())
    print("",pagedata.has_previous())
    # print("",pagedata.previous_page_number())###在访问页码是1的页面的时候是会报错的 就是他的页码至少是1
    ####这是pageid 这一页的数据
    return render(request,'myapp/showpage.html',{"sharedata":pagedata })
####测试ajax Jsonreponse

def showajax(request):
    alllist=Share.objects.all()


    return render(request,'myapp/ajaxtest.html',{"length":alllist})

from django.http import JsonResponse

def putajax(request):
    # print(request.POST)
    print(request.path)
    alllist = Share.objects.all()
    lists=[]
    for i in alllist:
        lists.append([i.title,i.keyword])
        #可以写入列表
    return JsonResponse({"data":lists})



########测试celery

import time
from .task import test
def celery(request):
    print(request.path)
    print(request.encoding)
    print(request.COOKIES)
    print(request.session)
    print(type(request.session))
    alllist = Share.objects.all()
    lists = []
    for i in alllist:
        lists.append([i.title, i.keyword])
        # 可以写入列表
    return JsonResponse({"data": lists})



####测试celery的使用
from celeryTest.sms.tasks import  send_email
from celery import Celery
from celeryTest.main import  app
def celery_test(request):



    ##异步任务的执行
    send_email.delay("jiang")
    #定时任务的执行
    # ctime = datetime.now()
    # # 默认用utc时间
    # utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
    # time_delay = timedelta(seconds=2)
    # task_time = utc_ctime + time_delay
    # result = send_email.apply_async(["jiiang", ], eta=task_time)
    # print(result.id)
    #
    # # time.sleep(2)

####设置10s 一运行的定时任务

    # app.conf.beat_schedule = {
    #     # 名字随意命名
    #     'add-every-10-seconds': {
    #         # 执行tasks1下的test_celery函数
    #         'task': 'celeryTest.sms.send_email',
    #         # 每隔2秒执行一次
    #         # 'schedule': 1.0,
    #         # 'schedule': crontab(minute="*/1"),
    #         'schedule': timedelta(seconds=3),
    #         # 传递参数
    #         'args': ('张三',)
    #     },
    #
    # }

    return  HttpResponse("jiangyuan is ok")


####复习views 的时候创建的
def getdata(request):
    a=request.GET.get("a")
    b=request.GET.get("b")
    c=request.GET.get("c")
    return HttpResponse("{}{:>10}{:>111}".format(a,b,c))

###复习views HttpResponse
def showResponse(request):

    print(request.session.get('name'))

    return HttpResponse('session is set successful')

from myapp.models import PutFile
######真的烦还是要重新来验证这个问题
def putfilequestion(request):
    # myfile=request.FILES.get("file",None)
    myfiles=request.FILES.getlist("file",None)
    for myfile in myfiles:
        PutFile.objects.create(ffilename=myfile.name,ffile=myfile)
    return HttpResponse("数据库已经写入")



#####测试img 或者file字段为空的情况
def blank(request):
    aaa=Share.objects.get(pk=3)
    myfile=request.FILES.get("files")
    ImgFile.objects.create(ffile=myfile,ffilename=myfile.name,Toblog=aaa)
    return HttpResponse("一个文件也能上传欸")


######验证码的使用

import random
from PIL import Image,ImageDraw,ImageFont
def getVerificationCode(request):
    # 创建画布
    # mode  模式,"RGB"
    # size  画布的尺寸
    image = Image.new("RGB", (200, 70), createcolor())###控制画布的尺寸
    imageDraw = ImageDraw.Draw(image, "RGB")
    # imageFont = ImageFont.truetype("/home/yc/Desktop/hz1805project/week01/static/fonts/ADOBEARABIC-ITALIC.OTF", size=50)
    imageFont = ImageFont.truetype("G:\\Inkfree.ttf", size=50)
    # imageDraw.text((5,10),"i love you!",fill=createcolor(),font=imageFont)
    import io
    charsource = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

    sum = ""
    for i in range(4):
        ch = random.choice(charsource)
        imageDraw.text((15 + i * 50, 10), ch, fill=createcolor(), font=imageFont)##第一个参数是xy轴，第二个是文本，第三个是颜色，第四个是字体
        sum += ch
    print(sum)
    # 通过session记录这个验证码并且设置过期时间为60秒
    request.session["verCode"] = sum ###把验证码的数字和字母存到session中
    request.session.set_expiry(60)
    # 画麻子
    for i in range(2000):
        x = random.randint(0, 200)
        y = random.randint(0, 70)
        imageDraw.point((x, y), fill=createcolor())

    # 创建一个字节流
    byteIO = io.BytesIO()
    # 把图片放在字节流里面去
    image.save(byteIO, "png")
    return HttpResponse(byteIO.getvalue(), "image/png")


# 随机颜色的生成
def createcolor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return (red, green, blue)


# 登陆页面
def login1(request):
    return render(request, "myapp/logincode.html")


# 登陆之后进行的后台比对操作
def dologin(request):
    value = request.GET.get("codevalue")
    value2 = request.session.get("verCode")

    try:
      if   value.lower() == value2.lower():######## 从前端传过来的value 是空得会引发nonetype 的错误

        return HttpResponse("success!!")
      else:
          return HttpResponse("error!!")
    except AttributeError:
        return  HttpResponse("请填入二维码")







####python3标准库的学习
def learnPost(request):
    result=request.POST.get("jiang")
    return HttpResponse(result)


####自定义模板的使用
def define(request):
    return render(request,'myapp/define.html')



from .forms import UserForm
####form 和user 相关应用
def showforms(request):
    form_obj=UserForm()
    if request.method=="POST":
        form_obj=UserForm(request.POST)
        if form_obj.is_valid():
            return   HttpResponse("成功")
    return render(request,'myapp/form_obj.html',{"form_obj":form_obj})

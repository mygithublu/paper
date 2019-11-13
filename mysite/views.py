from django.shortcuts import render,redirect
from django.http import JsonResponse
from mysite.models import title,record,record_mark,zzuser,app_vesion
import pandas as pd
import numpy as np
from numpy import nan as NaN
import os
import json
from django.http import FileResponse #文件下载
# Create your views here.



#登陆验证api
def login_api(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username)
    print(password)
    p=zzuser.objects.filter(psn=username,password=password)
    data={}
    if(p):
        data['res']=1
        return JsonResponse(data)
    else:
        data['res']=0
        return JsonResponse(data)

#检查更新api
def checkupdate_api(request):
    date=app_vesion.objects.all().values()
    vesion=date[0]['appvesion']
    data={}
    data['vesion']=vesion
    return JsonResponse(data)



def index(request):
    # title.objects.create(title_name='______负责现场不合格品零件（包括未经标识或可疑状态下的零件）的标识、隔离；以及可疑品/不合格品处理单中零件信息的填写，并参与不合格品审理',\
    # title_class='1',type='1',A='A、生产班组长',B='B、生产工段长',C='C、工程师',D='',answer='A、生产班组长',score='5')

    # title.objects.create(title_name='质量保证部整车质保科工程师负责判断报废物料责任，如果产生争议，________应及时联系相关质量保证部整车质保科________',\
    # title_class='1',type='1',A='A、班组长/VQ',B='B、工段长/SQE',C='C、工段长/VQ',D='',answer='C、工段长/VQ',score='5')

    # title.objects.create(title_name='Pilot工程师在车辆全部下线后发布本轮造车的M-BIR问题',\
    # title_class='1',type='3',A='',B='',C='',D='',answer='错误',score='5')

    # title.objects.create(title_name='PP阶段开始，涉及匹配的工段负责人在线上造车跟线时需带上打印好的CVIS，测量并记录数据',\
    # title_class='1',type='3',A='',B='',C='',D='',answer='正确',score='5')

    # zzuser.objects.create(psn='tt',password='1234',title_class='1',total='0')

    return render(request,'index.html')

#获取题目api
def ti_api(request):
    data={}
    #查询所有的题目
    # date=title.objects.all()[:1].values()
    psn=request.POST.get('username')
    #获取分数
    p=zzuser.objects.filter(psn=psn).values()
    total=p[0]['total']
    
    title_class=p[0]['title_class']

    #查询没有答过的题目，每次获取一条
    # date=title.objects.exclude(id__in=record_mark.objects.all().values_list('title_id',flat = True)).filter(title_class=title_class)[:1].values()
    # 20191024区分用户和区分
    date=title.objects.exclude(id__in=record_mark.objects.filter(psn=psn).values_list('title_id',flat = True)).filter(title_class=title_class)[:1].values()
    data['ti']=list(date)

   
    # count=title.objects.exclude(id__in=record_mark.objects.all().values_list('title_id',flat = True)).count()
    #获取条数
    # 20191024区分用户和区分
    count=title.objects.exclude(id__in=record_mark.objects.filter(psn=psn).values_list('title_id',flat = True)).filter(title_class=title_class).count()

    data['total']=total
    data['count']=count

    return JsonResponse(data)


#答题提交
def submit_api(request):
    #获取提交的信息
    psn=request.POST.get('psn')
    title_name=request.POST.get('title_name')
    answer=request.POST.get('answer')
    score=request.POST.get('score')
    title_id=request.POST.get('title_id')

    #获取用户累计分数,并更新总分数
    p=zzuser.objects.filter(psn=psn).values()
    total=p[0]['total']
    total=int(total)+int(score)
    zzuser.objects.filter(psn=psn).update(total=total)

    #写入答题记录表
    record.objects.create(psn=psn,title_name=title_name,answer=answer,score=score)
    #写入答题标记表
    record_mark.objects.create(psn=psn,title_id=title_id)
    data={}
    data['res']='ok'
    return JsonResponse(data)

def again_api(request):
    psn=request.POST.get('psn')
    record_mark.objects.filter(psn=psn).delete()
    data={}
    data['res']='ok'
    return JsonResponse(data)


#后台
def user(request):
    return render(request,'user.html')

#用户删除
def user_delete_api(request):
    #单个删除
    if(request.POST.get('id')):
        id=request.POST.get('id')
        print(id)
        zzuser.objects.filter(id=id).delete()
        return redirect('/user/')
    #批量删除
    else:
        date=request.POST.get('data')
        date=json.loads(date)
        for i in date:
            id=i['id']
            zzuser.objects.filter(id=id).delete()
        return redirect('/user/')




def user_pc_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    #工号查询
    if(request.GET.get('psn')):
        psn=request.GET.get('psn')
        date=zzuser.objects.filter(psn=psn)[s:e].values()
        data = {}
    #获取数据条数
        count=zzuser.objects.filter(psn=psn).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)
    else:
        date=zzuser.objects.all()[s:e].values()
        data = {}
        #获取数据条数
        count=zzuser.objects.all().count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)


def title_pc(request):
    return render(request,'title.html')


def record_pc(request):
    return render(request,'record.html')


#题目删除api
def title_delete_api(request):
        #单个删除
    if(request.POST.get('id')):
        id=request.POST.get('id')
        print(id)
        title.objects.filter(id=id).delete()
        return redirect('/title_pc/')
    #批量删除
    else:
        date=request.POST.get('data')
        date=json.loads(date)
        for i in date:
            id=i['id']
            title.objects.filter(id=id).delete()
        return redirect('/title_pc/')



#答题记录删除
def record_delete_api(request):
            #单个删除
    if(request.POST.get('id')):
        id=request.POST.get('id')
        print(id)
        record.objects.filter(id=id).delete()
        return redirect('/record_pc/')
    #批量删除
    else:
        date=request.POST.get('data')
        date=json.loads(date)
        for i in date:
            id=i['id']
            record.objects.filter(id=id).delete()
        return redirect('/record_pc/')

def title_pc_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit

    #区分查询
    if(request.GET.get('title_class') and request.GET.get('title_type')):
        title_class=request.GET.get('title_class')
        title_type=request.GET.get('title_type')
        date=title.objects.filter(title_class=title_class,title_type=title_type)[s:e].values()
        data = {}
    #获取数据条数
        count=title.objects.filter(title_class=title_class,title_type=title_type).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)
    elif(request.GET.get('title_class')):
        title_class=request.GET.get('title_class')
        date=title.objects.filter(title_class=title_class)[s:e].values()
        data = {}
    #获取数据条数
        count=title.objects.filter(title_class=title_class).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)       

    elif(request.GET.get('title_type')):
        title_type=request.GET.get('title_type')
        date=title.objects.filter(title_type=title_type)[s:e].values()
        data = {}
    #获取数据条数
        count=title.objects.filter(title_type=title_type).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)       

    else:
        date=title.objects.all()[s:e].values()
        data = {}
        #获取数据条数
        count=title.objects.all().count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)

def record_pc_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    #设备编号查询
    if(request.GET.get('psn')):
        psn=request.GET.get('psn')
        date=record.objects.filter(psn=psn)[s:e].values()
        data = {}
    #获取数据条数
        count=record.objects.filter(psn=psn).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)
    else:
        date=record.objects.all()[s:e].values()
        data = {}
        #获取数据条数
        count=record.objects.all().count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)



#用户导入并创建
def user_upload_file(request):
    myFile = request.FILES.get('myfile', None)         
    excelFile = open('D:/paper/upload/user/'+ myFile.name, 'wb+')
    for chunk in myFile.chunks():
        excelFile.write(chunk)
        excelFile.close()
    #创建用户
    df=pd.read_excel('D:/paper/upload/user/'+ myFile.name)
    #替换nan值为空字符串
    df=df.fillna('')
    row=df.shape[0]
    for i in range(row):
        psn=df.iloc[i,0]
        name=df.iloc[i,1]
        title_class=df.iloc[i,2]
        zzuser.objects.create(psn=psn,password='123456',name=name,title_class=title_class,total='0',rank='0',today_total='0')

    data = {}
    data['code']=0
    data['msg']=""
    data['data']='ok'
    return JsonResponse(data)

#导入试题
def tt_upload_file(request):
    myFile = request.FILES.get('myfile', None)         
    excelFile = open('D:/paper/upload/title/'+ myFile.name, 'wb+')
    for chunk in myFile.chunks():
        excelFile.write(chunk)
        excelFile.close()
    #创建题目
    df=pd.read_excel('D:/paper/upload/title/'+ myFile.name)
    #替换nan值为空字符串
    df=df.fillna('')
    row=df.shape[0]
    for i in range(row):
        title_name=df.iloc[i,0]
        title_class=df.iloc[i,1]
        title_type=df.iloc[i,2]
        A=df.iloc[i,3]
        B=df.iloc[i,4]
        C=df.iloc[i,5]
        D=df.iloc[i,6]
        answer=df.iloc[i,7]
        score=df.iloc[i,8]
        title.objects.create(title_name=title_name,title_class=title_class,title_type=title_type,A=A,B=B,C=C,D=D,answer=answer,score=score)

    data = {}
    data['code']=0
    data['msg']=""
    data['data']='ok'
    return JsonResponse(data)

def user_templates_download(request):
    file=open('D:/paper/templates/user.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="user.xlsx"'
    return response


def ti_templates_download(request):
    file=open('D:/paper/templates/paper.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="paper.xlsx"'
    return response
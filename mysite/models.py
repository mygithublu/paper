from django.db import models

# Create your models here.
class zzuser(models.Model):
    psn=models.CharField('工号',null=False,unique=True,max_length=10)
    name=models.CharField('姓名',null=True,max_length=10)
    password=models.CharField('密码',null=False,max_length=15)
    title_class=models.CharField('题库区分(1:生产2：维修3:工程)',null=False,max_length=10)
    total=models.CharField('累计总分',null=True,max_length=20)
    today_total=models.CharField('当天得分',null=True,max_length=10)
    rank=models.CharField('排名',null=True,max_length=10)
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        ordering = ['id']


class title(models.Model):
    title_name=models.CharField('题目',null=False,max_length=200)
    title_class=models.CharField('题库区分(1:生产2：维修3:工程)',null=False,max_length=10)
    title_type=models.CharField('类型（1：单选2：填空3：判断）',null=False,max_length=10)
    A=models.CharField('选项A',null=True,max_length=50)
    B=models.CharField('选项B',null=True,max_length=50)
    C=models.CharField('选项C',null=True,max_length=50)
    D=models.CharField('选项D',null=True,max_length=50)
    answer=models.CharField('答案',null=False,max_length=50)
    score=models.CharField('分数',null=False,max_length=10)
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
         ordering = ['id']

class record(models.Model):
    psn=models.CharField('工号',null=False,max_length=10)
    title_name=models.CharField('题目',null=False,max_length=200)
    answer=models.CharField('答案',null=False,max_length=50)
    score=models.CharField('得分',null=False,max_length=5)
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        ordering = ['id']

class record_mark(models.Model):
    title_id=models.CharField('题目ID',null=False,max_length=20)
    psn=models.CharField('工号',null=False,max_length=10)
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        ordering = ['id']

class app_vesion(models.Model):
    appvesion=models.CharField('版本号',null=False,max_length=20)
    class Meta:
        ordering=['id']
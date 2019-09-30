# Generated by Django 2.2 on 2019-09-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_record_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='zzuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psn', models.CharField(max_length=10, verbose_name='工号')),
                ('password', models.CharField(max_length=15, verbose_name='密码')),
                ('title_class', models.CharField(max_length=10, verbose_name='题库区分(1:生产2：维修3:工程)')),
                ('total', models.CharField(max_length=20, null=True, verbose_name='累计总分')),
                ('today_total', models.CharField(max_length=10, null=True, verbose_name='当天得分')),
                ('rank', models.CharField(max_length=10, null=True, verbose_name='排名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
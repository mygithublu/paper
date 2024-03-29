# Generated by Django 2.2 on 2019-09-17 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='题目')),
                ('title_class', models.CharField(max_length=10, verbose_name='题库区分(1:生产2：维修3:工程)')),
                ('type', models.CharField(max_length=10, verbose_name='类型（1：单选2：填空）')),
                ('score', models.CharField(max_length=10, verbose_name='分数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]

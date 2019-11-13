"""paper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
# from mysite.views import index,ti_api,submit_api,login_api,again_api,user,user_pc_api,title_pc,title_pc_api,user_upload_file,record_pc_api,record_pc,tt_upload_file,checkupdate_api,user_delete_api
from mysite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'index/',index),
    url(r'ti_api',ti_api),
    url(r'submit_api',submit_api),
    url(r'login_api',login_api),
    url(r'again_api',again_api),
    url(r'user/',user),
    url(r'user_pc_api',user_pc_api),
    url(r'title_pc_api',title_pc_api),
    url(r'title_pc/',title_pc),
    url(r'user_upload_file/',user_upload_file),
    url(r'record_pc_api',record_pc_api),
    url(r'record_pc/',record_pc),
    url(r'tt_upload_file/',tt_upload_file),
    url(r'checkupdate_api/',checkupdate_api),
    url(r'user_delete_api/',user_delete_api),
    url(r'title_delete_api/',title_delete_api),
    url(r'record_delete_api/',record_delete_api),
    url(r'record_delete_api/',record_delete_api),
    url(r'user_templates_download',user_templates_download),
    url(r'ti_templates_download',ti_templates_download),
]

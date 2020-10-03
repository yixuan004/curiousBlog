from django.shortcuts import render
import os
import json
import requests
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
def home(request):
    import requests
    import json

    return render(request,'home.html',{})

def company(request):
    
    inputCompanyName = request.POST['inputCompanyName']

    return render(request,'company.html',{'inputCompanyName':inputCompanyName})

def upload(request):

    if request.method == 'POST':
        obj = request.FILES.get("test.file")
        f = open(os.path.join(settings.MEDIA_ROOT,"upload",obj.name),'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()

        result = {"result":"OK", "filename":obj.name, "media_root":os.path.join(settings.MEDIA_ROOT,"upload")}
        #result = {}

        return HttpResponse(json.dumps(result))

def update(request):
    
    updateText20201003 = '20201003-实现了初步的页面的搜索跳转功能；实现了初步的附件上传功能（暂未给出图形化界面，可通过postman进行请求构造）目前可通过访问/media/upload/202010刘逸轩简历.pdf查看“关于我”；完成了home页面的初步排版；链接数据库可以进行数据库的查询（/company/页）'
    updateText = [updateText20201003]

    return render(request, 'updateDescription.html', {'updateText':updateText})


def companyInfoAll(request):
    from . import models

    companyInfoObj = models.companyInfo.objects.all()
    return render(request,'dbTest.html',{'li':companyInfoObj})
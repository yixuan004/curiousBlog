from django.shortcuts import render
import os
import json
import requests
from django.http import HttpResponse
from django.conf import settings
from . import models

# Create your views here.
def home(request):
    import requests
    import json

    #在home页随机返回3条数据，不支持两个函数连接到同一个html中
    companyInfoObjs = models.companyInfo.objects.order_by('?')[:3] # 数据库中的随机3条数据
    
    return render(request,'home.html',{'first':companyInfoObjs[0], 'second':companyInfoObjs[1], 'third':companyInfoObjs[2]})

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
    
    updateText20201003 = '20201003-实现了初步的页面的搜索跳转功能；实现了初步的附件上传功能（暂未给出图形化界面，可通过postman进行请求构造）\
    目前可通过访问/media/upload/202010刘逸轩简历.pdf查看“关于我”；完成了home页面的初步排版；链接数据库可以进行数据库的查询（/company/页）；\
    实现了基础的翻页功能并对翻页样式进行了优化；在home页会随机展示3条公司-时间-新闻的对应关系并进行了排版的优化'
    updateText = [updateText20201003]

    return render(request, 'updateDescription.html', {'updateText':updateText})


def companyInfoAll(request):
    from . import models
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    companyInfoObj = models.companyInfo.objects.all() # 数据库中的全部数据
    
    page = Paginator(companyInfoObj, 20) # 每页展示20条数据，目前在这里写死，希望做成用户可选择的导航条，通过用户的选择展示每页5 or 10 or 20条数据
    page_id = request.GET.get('page_id')
    
    around = 5 # 设置一个定值，为翻页栏的前后5条会被显示出来

    if page_id:
        try:
            companyInfoObjs = page.page(page_id)
            #current = companyInfoObjs.number  # 唯一try成功不异常，作为当前的页码
        except PageNotAnInteger:
            companyInfoObjs = page.page(1)
        except EmptyPage:
            companyInfoObjs = page.page(1)
    else:
        companyInfoObjs = page.page(1)

    total = page.num_pages # 总共的页码
    current = companyInfoObjs.number

    # 在后端进行处理，返回{'left_has_more': left_has_more, 'right_has_more': right_has_more, 'left_page_range': left_page_range, 'right_page_range': right_page_range }
    if current <= around + 3:
        left_has_more = False
        left_page_range = range(1, current)
    else:
        left_has_more = True
        left_page_range = range(current - around, current)

    if current >= total - around - 2:
        right_has_more = False
        right_page_range = range(current + 1, total + 1)
    else:
        right_has_more = True
        right_page_range = range(current + 1, current + around + 1)

    #print("locals()", locals())
 
    return render(request,'dbTest.html',locals()) # locals() 函数会以字典类型返回当前位置的全部局部变量。
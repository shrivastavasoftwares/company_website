from django.shortcuts import render
from .models import blog,services,basic_info,projects,products
from django.http import HttpResponse

# Create your views here.
def base(request):
    MEDIA_URL = '/media/'

    data=basic_info.objects.get(id=1)
    return render(request,'base.html',{"data":data,"MEDIA_URL":MEDIA_URL})

def about(request):
    return render(request,'about.html')

def service_fun(request,id):
    try:

        s=services.objects.get(id=id)
    except:
        return HttpResponse("Not found")



    return render(request,'services.html',{'s':s})

def blog_fun(request):
    data=blog.objects.all()
    MEDIA_URL = '/media/'

    return render(request,'blog.html',{'data':data,"MEDIA_URL":MEDIA_URL})

def projects_fun(request):
    data=projects.objects.all()
    return render(request,'OurProject.html',{'data':data})


def products_fun(request):
    data=products.objects.all()
    return render(request,'ourproducts.html',{'data':data})
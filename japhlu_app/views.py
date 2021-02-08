from django.shortcuts import render
from .models import blog,services,basic_info,projects,products
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request,'base.html')

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

    return render(request,'blog.html',{'data':data})

def projects_fun(request):
    data=projects.objects.all()
    return render(request,'OurProject.html',{'data':data})


def products_fun(request):
    data=products.objects.all()
    return render(request,'ourproducts.html',{'data':data})
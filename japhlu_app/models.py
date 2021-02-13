from django.db import models
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import  RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.
class blog(models.Model):
    Title=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    img=models.ImageField(upload_to='media/img',blank=True,null=True)
    content = RichTextField(null=True,blank=True)




class basic_info(models.Model):
    phone_no=models.CharField(max_length=12,null=True,blank=True)
    Address=models.TextField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    image_1=models.ImageField(upload_to='media/img',blank=True,null=True)
    image_2=models.ImageField(upload_to='media/img',blank=True,null=True)
    image_3=models.ImageField(upload_to='media/img',blank=True,null=True)



class projects(models.Model):
    Title=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    deploy_url=models.URLField(null=True,blank=True)
    content = RichTextField(null=True,blank=True)


    create_date=models.DateField(null=True,blank=True)
    update_date=models.DateField(null=True,blank=True)


class products(models.Model):
    Title=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    content = RichTextField(null=True,blank=True)

    deploy_url=models.URLField(null=True,blank=True)
    create_date=models.DateField(null=True,blank=True)
    update_date=models.DateField(null=True,blank=True)


class services(models.Model):
    Title=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    service_description=models.TextField(null=True,blank=True)
    content = RichTextField(null=True,blank=True)

    img=models.ImageField(upload_to='media/img',blank=True,default="blank-headshot.jpg")
    #hi=models.CharField(max_length=100,null=True,blank=True)




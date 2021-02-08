__author__ = 'PRIYANSH KHANDELWAL'
from django.urls import path
from japhlu_app import views

app_name='Main_app'
urlpatterns = [
    path('',views.base,name='home'),
        path('about/',views.about,name='about'),
            path('service/<int:id>/',views.service_fun,name='service'),
                path('blog/',views.blog_fun,name='blog'),
    path('products/',views.products_fun,name='products'),
    path('projects/',views.projects_fun,name='projects'),





]
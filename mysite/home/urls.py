from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blogs',views.blogs,name='blogs'),
    path('contact',views.contact,name='contact'),
]

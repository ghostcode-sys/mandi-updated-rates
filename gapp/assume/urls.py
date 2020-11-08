from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('search', views.search, name='search'),
    path('usign', views.usign, name='sign'),
    path('alog', views.alog, name='alog'),
    path('alogin', views.alogin, name='alogin'),
    path('crop', views.crop, name='crop'),
    path('ulogin', views.ulogin, name='ulogin'),
    path('contact', views.contact, name='contact'),
]
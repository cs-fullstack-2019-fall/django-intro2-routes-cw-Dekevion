from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gogetthegood',views.getgood,name='good'),
    path('happyhappyjoyjoy',views.joy,name='joy')
]
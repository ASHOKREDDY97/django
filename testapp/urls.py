from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name ='home'),
    path('index/',views.index,name='index'),
    path('choice/',views.choice,name='choice'),
    path('forms/',views.forms,name='forms'),
]





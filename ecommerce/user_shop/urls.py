from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('index',views.home,name='home'),
    path('high',views.high,name='high'),
    path('low',views.low,name='low')
]
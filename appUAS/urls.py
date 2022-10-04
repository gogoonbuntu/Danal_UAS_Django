from django.urls import path 
from . import views 

app_name = 'appUAS'

urlpatterns=[
    path('Ready', views.ready),
    path('CPCGI', views.cpcgi),
    path('Success', views.success),
    path('BackURL', views.backurl),
]
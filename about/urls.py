from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.view_about_page, name='about'),
    path('farm/', views.view_farm_page, name='farm'),
    path('flavours/', views.view_flavours_page, name='flavours'),
]

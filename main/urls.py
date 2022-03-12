from turtle import home
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import main

urlpatterns = [
    path('', views.homepage, name='index'),
    path('collab/', views.collab, name='index'),
    path('company/', views.company, name='index'),
    path('profile/', views.profile, name='index'),
    path('service/', views.service, name='index'),
    path('v1/', views.v1, name='index'),
]

urlpatterns += staticfiles_urlpatterns()

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base-home'),
    path('test/', views.test, name='base-test'),
    path('test1/', views.test1, name='base-test1'),
]

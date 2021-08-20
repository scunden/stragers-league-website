from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base-home'),
    path('info/', views.info, name='base-info'),
    path('draft/', views.draft, name='base-draft'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.nexusHome, name='nexusHome'),
]
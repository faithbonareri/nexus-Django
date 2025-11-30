from django.urls import path
from . import views

urlpatterns = [
    path('produce', views.produceSector )
]
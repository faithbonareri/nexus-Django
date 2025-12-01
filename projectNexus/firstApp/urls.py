from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('create-shoe/', views.createShoe, name='createShoe'), # New Route
]
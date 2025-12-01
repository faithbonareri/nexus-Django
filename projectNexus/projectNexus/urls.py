from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Change 'firstApp/' to '' so it loads at the root homepage
    path('', include('firstApp.urls')), 
]
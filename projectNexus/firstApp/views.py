from django.shortcuts import render
from .models import Shoes

def nexusHome(request):
    # ORM: "Select * from Shoes"
    shoes = Shoes.objects.all() 
    # Context: Passing data from Python to HTML
    context = {'shoes': shoes}
    return render(request, 'firstApp/home.html', context)
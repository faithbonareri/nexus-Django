from django.shortcuts import render, redirect # Import redirect
from .models import Shoes
from .forms import ShoeForm # Import the form

def home(request):
    return render(request, 'firstApp/home.html')

def market(request):
    shoes = Shoes.objects.all()
    context = {'shoes': shoes}
    return render(request, 'firstApp/market.html', context)

def createShoe(request):
    form = ShoeForm()
    
    # Check if the user is sending data (POST) or just visiting (GET)
    if request.method == 'POST':
        form = ShoeForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('market') # Redirect to the market list

    context = {'form': form}
    return render(request, 'firstApp/form.html', context)
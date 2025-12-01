from django.forms import ModelForm
from .models import Shoes

class ShoeForm(ModelForm):
    class Meta:
        model = Shoes
        fields = '__all__'
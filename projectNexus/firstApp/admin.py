from django.contrib import admin
from .models import Shoes, Bags, Clothes

# Create a configuration class for Shoes
class ShoeAdmin(admin.ModelAdmin):
    # This controls what columns show up in the list
    list_display = ('name', 'size', 'created_at') 
    
    # This adds a search bar at the top!
    search_fields = ('name', 'description')

# Register the model WITH the configuration
admin.site.register(Shoes, ShoeAdmin)
admin.site.register(Bags)
admin.site.register(Clothes)
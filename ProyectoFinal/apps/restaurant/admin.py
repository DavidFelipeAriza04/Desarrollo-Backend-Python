from django.contrib import admin
from .models import Restaurant, Product

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'owner')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost_per_unit', 'all_restaurants')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Product, ProductAdmin)
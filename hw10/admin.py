from django.contrib import admin    # noqa:F401

from .models import City, Customer, Product, Supplier


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_id']

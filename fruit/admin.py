from django.contrib import admin
from .models import Fruit, Customers
#FruitFarmer
from import_export.admin import ImportExportModelAdmin

@admin.register(Fruit)
class FruitAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'count']
    list_display_links = ['id', 'title', 'description', 'price', 'count']
    ordering = ['-price', 'title']
    search_fields = ['title', 'description']
    filter = ['title']

@admin.register(Customers)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ["id", "first_name", "last_name", "role"]
    search_fields = ["first_name", "last_name", "role"]

# @admin.register(FruitFarmer)
# class FruitFarmerAdmin(ImportExportModelAdmin):
#     list_display = ("id", "customer", 'fruit', 'is_returned', "create_date")
#    # list_display_links = ["id", "customer", "fruit", "took_on", "create_date"]
#     autocomplete_fields = ("fruit",)
#     search_fields = ("customer", "fruit")
# # Register your models here.
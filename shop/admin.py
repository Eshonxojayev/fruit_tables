from django.contrib import admin
from .models import Fruits, Aunts

@admin.register(Aunts)
class AuntsAdmin(admin.ModelAdmin):
    list_display = ("title", "total_fruit")


@admin.register(Fruits)
class FruitsAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "rayting", "status", "create_date")
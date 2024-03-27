from django.urls import path
from .views import FruitListView, FruitDetailView, AddFruitView, FruitSettingsView, FruitDeleteView

urlpatterns = [
    path('fruit/', FruitListView.as_view(), name="fruit"),
    path("fruit/<int:id>/", FruitDetailView.as_view(), name="detail"),
    path("addfruits/", AddFruitView.as_view(), name="add-fruit"),
    path("fruitsettings/<int:id>/", FruitSettingsView.as_view(), name="settings-fruit"),
    path("fruitdelete/<int:id>/", FruitDeleteView.as_view(), name="fruit-delete"),
]
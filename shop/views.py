from django.shortcuts import render
from django.views import View
from .models import Fruits, Aunts

class LandingPageView(View):
    def get(self, request):
        aunts = Aunts.objects.all()
        fruit = Fruits.objects.all()
        context = {
            'aunts': aunts,
            'fruit': fruit
        }
        return render(request, 'landing.html', context)
# Create your views here.

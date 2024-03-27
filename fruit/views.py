from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Fruit
from .forms import AddFruitModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

class FruitListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            fruits = Fruit.objects.all()
            context = {
                "fruit": fruits
            }
            return render(request, "shop/fruit.html", context)
        else:
            fruit = Fruit.objects.filter(title__icontains=search)
            if not fruit:
                return HttpResponse("<h3>Not Fount</h3>")
            else:
                context = {
                    "fruit": fruit,
                    "search": search
                }
                return render(request, "shop/fruit.html", context)

class FruitDetailView(View):
    def get(self, request, id):
        fruit = Fruit.objects.get(id=id)
        return render(request, "shop/fruit_detail.html", context={"fruit": fruit})

class AddFruitView(View):
    def get(self, request):
        form = AddFruitModelForm()
        context = {
            "form": form
        }
        return render(request, "shop/add_fruit.html", context)

    def post(self, request):
        # title = request.POST["title"]
        # description = request.POST["description"]
        # image = request.POST["image"]
        # count = request.POST["count"]
        # price = request.POST["price"]
        # data = {
        #     "title": title,
        #     "description": description,
        #     "image": image,
        #     "count": count,
        #     "price": price,
        # }
        # print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,{data} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        form = AddFruitModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("fruits")
        else:
            form = AddFruitModelForm()
            context = {
                "form": form
            }
            return render(request, "shop/add_fruit.html", context)

class FruitSettingsView(View):
    def get(self, request, id):
        fruit = Fruit.objects.get(id=id)
        # form = AddBookModelForm()
        context = {
            "fruit": fruit
        }
        return render(request, "shop/setting.html", context)

    def post(self, request, id):
        # form = AddBookModelForm(data=request.POST)
        title = request.POST["title"]
        description = request.POST["description"]
        count = request.POST["count"]
        price = request.POST["price"]
        image = request.POST["image"]

        fruit = Fruit.objects.get(id=id)
        fruit.title = title
        fruit.description = description
        fruit.count = count
        fruit.price = price
        fruit.image = f"shop/author/{image}"

        fruit.save()

        return redirect("fruits")
        # else:
        #     book = Book.objects.get(id=id)
        #     # form = AddBookModelForm()
        #     context = {
        #         "book": book
        #     }
        #     return render(request, "library/settings_book.html", context)


class FruitDeleteView(View):
    def get(self, id):
        fruit = Fruit.objects.get(id=id)
        fruit.delete()
        return redirect("fruits")
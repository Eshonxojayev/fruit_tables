from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Fruit(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField()
    price = models.FloatField(default=1)
    image = models.ImageField(upload_to="fruit")
    count = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)

    def __str__(self):
        return f"{self.title}"

# class Customers(models.Model):
#     ROLE = (
#         ("client", "C"))
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     role = models.CharField(max_length=20, choices=ROLE, default="C")
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# class FruitFarmer(models.Model):
#     customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
#     fruits = models.ForeignKey(Fruit, on_delete=models.CASCADE)
#     took_on = models.DateField()
#     returned_on = models.DateField(null=True, blank=True)
#     create_date = models.DateTimeField(auto_now=True)
#
#     def is_returned(self):
#         return self.returned_on is not None

# class Author(models.Model):
#     first_name = models.CharField(max_length=20, null=True)
#     last_name = models.CharField(max_length=20, null=True)
#     image = models.ImageField(upload_to="shop/authors/")
#     publish_date = models.DateField(auto_now_add=True)
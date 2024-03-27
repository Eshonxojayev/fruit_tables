from django.db import models

class Aunts(models.Model):
    title = models.CharField(max_length=50)
    total_fruit =models.PositiveIntegerField()
    image = models.ImageField(upload_to='course/aunts/')

    def __str__(self):
        return self.title

class FruitRole(models.TextChoices):
    DRAFT = ("Ko'rinmasin", "Ko'rinmasin")
    Publish = ("Ko'rinsin", "ko'rinsin")

class Fruits(models.Model):
    title = models.CharField(max_length=100)
    aunt = models.ForeignKey(Aunts, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fruit/fruits/')
    price = models.FloatField()
    rayting = models.FloatField(default=0.0)
    status = models.CharField(max_length=20, choices=FruitRole.choices, default=FruitRole.Publish)
    create_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

# Create your models here.

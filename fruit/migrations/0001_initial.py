# Generated by Django 5.0.3 on 2024-03-27 11:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('price', models.FloatField(default=1)),
                ('image', models.ImageField(upload_to='fruit')),
                ('count', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]

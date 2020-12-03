import os 
import django
from pizza.models import Pizza, Topping

os.environ.setdefalt("DJANGO_SETTINGS_MODULE", "pizzeria.settings")
django.setup()

pizza = Pizza.objects.all()

for p in pizza:
    print("Pizza ID:", pizza.id, "Pizza:", pizza)

topping = t.topping_set.all()

for t in topping:
    print(t)
import os 
import django
from pizza.models import Pizza

os.environ.setdefalt("DJANGO_SETTINGS_MODULE", "pizzeria.settings")
django.setup()

pizza = Pizza.objects.all()

for p in pizza:
    print("Pizza ID:", pizza.id, "Pizza:", pizza)

t = Pizza.objects.get(id=1)
print(t.name)
print(t.date_added)

topping = t.topping_set.all()

for t in topping:
    print(t)
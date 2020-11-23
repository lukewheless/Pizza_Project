import os 
import django

os.environ.setdefalt("DJANGO_SETTINGS_MODULE", "pizzeria.settings")
django.setup()

from pizza.models import Pizza

pizza = Pizza.objects.all()

for p in pizza:
    print("Pizza ID:", pizza.id, "Pizza:", pizza)

p = Pizza.objects.get(id=1)
print(p.text)
print(p.date_added)

toppings = p.entry_set.all()

for t in toppings:
    print(t)
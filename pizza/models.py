from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    #allows to set it to toppings when more than one topping is added
    
    class Meta:
        verbose_name_plural = 'toppings'

    def _str_(self):
        return f"{self.name[:50]}..."
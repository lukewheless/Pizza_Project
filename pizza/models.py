from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name # instance of the class

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE) # has a fk with Pizza to create relational database
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE) #same as topping
    name = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
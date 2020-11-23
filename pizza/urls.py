from django.urls import path
from . import views

app_name = 'pizza'

urlpatterns = [
    path('', views.index, name="index"),
    path('pizza', views.pizza, name="pizza"),
    path('pizza/<int:pizza_id>/', views.pizza, name="pizza"),
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping'),
]
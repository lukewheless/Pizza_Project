from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, NewEntry

# Create your views here.
def index(request):
    return render(request,'pizza/index.html')

#to get all pizzas
def pizza(request):
    pizza = Pizza.objects.order_by("date_added")

    context = {'Pizzas': pizza}

    return render(request,'pizza/pizza.html', context)

#individual toppings
def topping(request, pizza_id):
    pizza = Pizza.objects.get(id=topic_id)
    toppings = pizza.entry_set.order_by("-date_added") # desc order (-)

    context = {'pizza': pizza, 'toppings': toppings}

    return render(request,'pizza/toppings.html', context)

#get read data from database
#post sends data to database

def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm() #blank form
    else:
        form = PizzaForm(data=request.POST) #all info from user onto form

        if form.is_valid():
            form.save()     #saves form directly to topic model

            return redirect('pizza:pizza')
    
    context = {'form':form}

    return render(request, 'pizza/new_pizza.html', context)

def new_topping(request, topic_id):
    pizza = Pizza.objects.get(id=topic_id)
    if request.method != 'POST':
        form = PizzaForm() #blank form
    else:
        form = ToppingForm(data=request.POST) #all info from user onto form

        if form.is_valid():
            new_topping = form.save(commit=False)     #saves form directly to topic model

            new_topping.topic = topic
            new_topping.save()
            form.save()
            return redirect('pizza:topping',pizza_id=pizza_id)
    
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizza/new_topping.html', context)
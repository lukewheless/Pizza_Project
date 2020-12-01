from django.shortcuts import render, redirect
from .models import Pizza
from .forms import PizzaForm, ToppingEntry

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
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.entry_set.order_by("-date_added") # desc order (-)

    context = {'pizza': pizza, 'toppings': toppings}

    return render(request,'pizza/topping.html', context)

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

def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = PizzaForm() #blank form
    else:
        form = ToppingForm(data=request.POST) #all info from user onto form

        if form.is_valid():
            new_topping = form.save(commit=False)     #saves form directly to topic model

            new_topping.pizza = pizza
            new_topping.save()
            form.save()
            return redirect('pizza:topping',pizza_id=pizza_id)
    
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizza/new_topping.html', context)

    def edit_topping(request, topping_id):
    topping = ToppingEntry.objects.get(id=topping_id)
    pizza = topping.pizza

    if request.method != 'POST':
        form = EntryForm(instance=topping) # loads form with existing entry 
    else:
        form = EntryForm(instance=topping, data=request.POST) 

        if form.is_valid():
            form.save()
            return redirect('pizza:pizza', pizza_id=pizza.id) 
    
    context = {'topping':topping, 'pizza':pizza, 'form':form} #function of context that shows us a view of data we want to see
    return render(request, 'pizza/edit_topping.html', context)
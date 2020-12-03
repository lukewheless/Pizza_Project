from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import PizzaForm, ToppingForm, CommentForm

# Create your views here.
def index(request):
    return render(request,'pizza/index.html')

#to get all pizzas
def pizzas(request):
    pizzas = Pizza.objects.order_by("-date_added")
    
    context = {'pizzas': pizzas}
    return render(request,'pizza/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    topping = pizza.topping_set.order_by("-date_added") # desc order (-)
    comment = pizza.comment_set.order_by('-date_added')
    
    context = {'pizza': pizza, 'topping': topping, 'comment': comment}
    return render(request,'pizza/pizza.html', context)

#get read data from database
#post sends data to database
def new_pizza(request, pizza_id):
    if request.method != 'POST':
        form = PizzaForm()                  #blank form
    else:
        form = PizzaForm(data=request.POST) #all info from user onto form

        if form.is_valid():
            form.save()                     #saves form directly to topic model

            return redirect('pizza:pizzas') #FLAG THIS (s)
    
    context = {'form':form}
    return render(request, 'pizza/new_pizza.html', context)

def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST) 

        if form.is_valid():
            form.save()     

            return redirect('pizza:pizza', pizza_id=pizza_id)
    
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizza/new_topping.html', context)
    

def edit_topping(request, topping_id):
    topping = ToppingForm.objects.get(id=topping_id)
    pizza = topping.pizza

    if request.method != 'POST':
        form = ToppingForm(instance=topping) # loads form with existing entry 
    else:
        form = ToppingForm(instance=topping, data=request.POST) 

    if form.is_valid():
        form.save()
        return redirect('pizza:pizza', pizza_id=pizza.id) 
    
    context = {'topping':topping, 'pizza':pizza, 'form':form} #function of context that shows us a view of data we want to see
    return render(request, 'pizza/edit_topping.html', context)

def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST) 

        if form.is_valid():
            form.save()     

            return redirect('pizza:pizza', pizza_id=pizza_id)
    
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizza/comment.html', context)
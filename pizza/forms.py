from django import forms 
from.models import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza 
        fields = ['name']
        labels = {'name':''}

class ToppingEntry(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'name':''}
        widgets = {'name': forms.Textarea(attrs={'cols': 80})}

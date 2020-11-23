from django import forms 
from.models import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Topic 
        fields = ['text']
        labels = {'text':''}

class ToppingEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

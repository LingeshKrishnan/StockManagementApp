from django import forms
from .models import *

class Nightyform(forms.ModelForm):
    class Meta:
        model = Nighty
        fields = ('type', 'price', 'status', 'issues')

class Inskirtform(forms.ModelForm):
    class Meta:
        model = Inskirt
        fields = ('type', 'price', 'status', 'issues')

class Blouseform(forms.ModelForm):
    class Meta:
        model = Blouse
        fields = ('type', 'price', 'status', 'issues')

class Sareeform(forms.ModelForm):
    class Meta:
        model = Saree 
        fields = ('type', 'price', 'status', 'issues')
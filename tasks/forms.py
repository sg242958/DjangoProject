from django import forms
from .models import *
class contact_form(forms.ModelForm):
        a = forms.CharField(widget=forms.TextInput(), max_length=20, required=True)
        b = forms.EmailField()
        c = forms.CharField(widget=forms.TextInput(), max_length=500, required=False)

        class Meta:
                model = Contact
                fields = ['a', 'b', 'c', 'Images', 'user']


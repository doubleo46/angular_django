from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()

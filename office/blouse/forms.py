from django import forms

class blouseform(forms.Form):
    category = forms.CharField(max_length=100)
    size = forms.IntegerField()
    price = forms.IntegerField()
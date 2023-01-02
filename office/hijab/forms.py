from django import forms

class hijabform(forms.Form):
    warna = forms.CharField(max_length=100)
    size = forms.CharField(max_length=5)
    price = forms.CharField(max_length=10)
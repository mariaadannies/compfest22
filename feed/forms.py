from django import forms

class PostForm(forms.Form):
    name = forms.CharField()

    image = forms.FileField()

    desc = forms.CharField()

    price = forms.DecimalField()
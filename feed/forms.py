from django import forms

class PostForm(forms.Form):
    name = forms.CharField()

    image = forms.FileField()

    desc = forms.CharField()

    price = forms.DecimalField()

class BalanceForm(forms.Form):
    add_amount = forms.DecimalField()

    withdraw_amount = forms.DecimalField()

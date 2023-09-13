from django import forms


class Registrationform(forms.Form):
    name =forms.CharField(max_length=100)
    Age  = forms.IntegerField()
    pw   =forms.CharField(max_length=123,widget=forms.PasswordInput)
    
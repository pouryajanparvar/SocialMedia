from django import forms


class UserRegistrationsForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField()
    password = forms.CharField()

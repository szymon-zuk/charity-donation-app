from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "name",
            "surname",
            "email",
            "password",
            "password2",
        ]
        labels = {
            "name": "Imię",
            "surname": "Nazwisko",
            "email": "E-mail",
            "password": "Hasło",
            "password2": "Powtórz hasło",
        }


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class DonationForm(forms.Form):
    quantity = forms.IntegerField()
    address = forms.CharField(max_length=128)
    phone_number = forms.IntegerField()
    city = forms.CharField(max_length=128)
    zip_code = forms.CharField(max_length=6)
    pick_up_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'RRRR-MM-DD'}))
    pick_up_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '--:--'}))
    pick_up_comment = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}), required=False)
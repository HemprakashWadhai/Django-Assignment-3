from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    pincode = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # name = forms.CharField(max_length=50)
    mobile = forms.CharField(max_length=12)
    # address = forms.CharField()
    # bank_details = forms.CharField()
    # education = forms.CharField()
    # username = forms.CharField()

    class Meta:
        model = Profile
        fields = ['username', 'email', 'mobile', 'password1', 'password2']
        # fields = ['username', 'email', 'name', 'mobile', 'address', 'bank_details', 'education', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=50)
    mobile = forms.CharField(max_length=12)
    address = forms.CharField()
    bank_details = forms.CharField()
    education = forms.CharField()
    username = forms.CharField()


    class Meta:
        model = Profile
        fields = ['username', 'email', 'name', 'mobile', 'address', 'bank_details', 'education']

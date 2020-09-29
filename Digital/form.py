from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1',
                  'password2']


class principalForm(ModelForm):
    class Meta:
        model = Principal
        fields = '__all__'


class bauturiForm(ModelForm):
    class Meta:
        model = Bauturi
        fields = '__all__'


class desertForm(ModelForm):
    class Meta:
        model = Desert
        fields = '__all__'

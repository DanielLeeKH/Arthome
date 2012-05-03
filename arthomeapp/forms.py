from models import *
from django import forms

class ArtworkForm (forms.ModelForm):
    class Meta:
	model = Artwork

class LoginForm (forms.Form):
   username = forms.CharField(label='Username or Password')
   password = forms.CharField(widget=forms.PasswordInput) 

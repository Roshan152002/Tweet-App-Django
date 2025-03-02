from django import forms
from .models import Tweets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ['tweet_msg','photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
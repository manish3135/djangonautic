from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))

    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
        'username': forms.TextInput(attrs={'class':'input','autofocus':True}),
        'email' :forms.EmailInput(attrs={'class':'input','required':True})
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
       model = UserProfileInfo
       fields = ('profile_pic',)

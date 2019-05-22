from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    #it is our provided password1 field and not of  from user table as user table
    # password  field is visible
    class Meta:
        model = User
        exclude=['password']
        fields = ['username','password1','email','first_name','last_name']

from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.models import

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    
    # widgets = {
    #         'username':forms.TextInput(attrs={'class':'form-control'}),
    #         'password': forms.PasswordInput(attrs={'class':'form-control'}),
    # }

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    
    
    
    
    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("This username is taken")
        return self.cleaned_data['username']
    
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Your passwords donot match")
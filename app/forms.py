from django import forms
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ckeditor.widgets import CKEditorWidget

class BlogUploadForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control'}))
    class Meta:
        model = Blog 
        fields = ['title', 'tags', 'content', 'image']
        
        labels = {
            'tags': 'Tag',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'tags': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'email']
        
        labels = {
            'first_name': 'Name',
            'email': 'Email',
        }
        
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        } 
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
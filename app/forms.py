from app.models import Post
from django import forms
from django.contrib.auth.models import User
class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = '__all__'

class Signup(forms.ModelForm):
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')
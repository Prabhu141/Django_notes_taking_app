from django import forms
from .models import Note, User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'user_name', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note_title', 'note_content']
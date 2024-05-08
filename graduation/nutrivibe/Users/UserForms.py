# myapp/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile_number']

    email = forms.EmailField(max_length=100)
    mobile_number = forms.CharField(max_length=15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removing help text for password fields
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None


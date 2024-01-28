from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile

def validate_email(form_email):
    if User.objects.filter(email = form_email).exists():
        raise ValidationError(f'{form_email} already exists in our system.', params={'form_email': form_email})
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(min_length=2, max_length=32)
    last_name = forms.CharField(min_length=2, max_length=32)
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2' ]
        widgets = {
            'car': forms.Select(),
        }


class ProfileForm(forms.ModelForm):
    website = forms.CharField(min_length=3, max_length=256)

    class Meta:
        model = UserProfile
        fields = ['website', 'car']
        
        widgets = {
            'car': forms.Select(),
        }

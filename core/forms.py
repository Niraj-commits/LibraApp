from django.contrib.auth.forms import UserCreationForm

from .models import *

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','password1','password2','email','role']
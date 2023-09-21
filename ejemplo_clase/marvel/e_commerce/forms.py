from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['pais','provincia','ciudad','codigo_postal','telefono_contacto']

    




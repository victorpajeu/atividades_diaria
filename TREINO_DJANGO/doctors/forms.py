from django import forms
from .models import Doctor


class DoctorForms(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'age', 'cpf']

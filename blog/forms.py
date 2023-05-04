from django import forms

from .models import Patient, Voiture, Employee


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'dateNaissance', 'malade']
    # widgets = {
    #     'nom': forms.TextInput(attrs={'class': 'form-control'}),
    #    'dateNaissance': forms.DateField(atr={'class': 'form-control'}),
    #   'malade': forms.CheckboxInput(at={'class': 'form-control'})
    # }


class CarsForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['marque', 'modele', 'type', 'color', 'doors', 'image', 'seats']
        widgets = {
            'marque': forms.TextInput(attrs={'class': 'form-control'}),
            'modele': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'doors': forms.TextInput(attrs={'class': 'form-control'}),
            'seats': forms.TextInput(attrs={'class': 'form-control'}),

        }


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['nom', 'username', 'password', 'role']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),

        }

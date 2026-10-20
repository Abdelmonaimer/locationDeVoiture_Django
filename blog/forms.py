from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient, Voiture, Employee, Client, Reservation


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


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'email', 'username', 'password']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['dateDebut', 'dateFin', 'prix', 'voiture']
        widgets = {
            'dateDebut': forms.DateInput(),
            'dateFin': forms.DateInput(),
            'prix': forms.TextInput(attrs={'class': 'form-control'}),
            'voiture': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    name = forms.TextInput(attrs={'class': 'form-control'}),
    email = forms.TextInput(attrs={'class': 'form-control'}),
    message = forms.TextInput(attrs={'class': 'form-control'}),

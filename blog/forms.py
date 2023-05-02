from django import forms


from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'dateNaissance', 'malade']
       # widgets = {
       #     'nom': forms.TextInput(attrs={'class': 'form-control'}),
        #    'dateNaissance': forms.DateField(atr={'class': 'form-control'}),
         #   'malade': forms.CheckboxInput(at={'class': 'form-control'})
        #}

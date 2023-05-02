from django.db import models


# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=50)
    dateNaissance = models.DateField()
    malade = models.BooleanField(default=False)





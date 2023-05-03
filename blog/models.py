from django.db import models


# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=50)
    dateNaissance = models.DateField()
    malade = models.BooleanField(default=False)


class Paiement(models.Model):
    totalPaye = models.FloatField()
    montantPaye = models.FloatField()
    class Meta:
        db_table = "Paiement"

    def __str__(self):
        return self.totalPaye + " " + self.montantPaye


class Facture(models.Model):
    paiement = models.ForeignKey(Paiement, on_delete=models.CASCADE, null=True)
    nbrJours = models.FloatField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    montant = models.FloatField()
    class Meta:
        db_table = "Facture"

    def __str__(self):
        return self.nom + " " + self.prenom + " " + self.montant + " " + self.nbrJours


class Voiture(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    color = models.CharField(max_length=50, null=True)
    seats = models.IntegerField( null=True)
    doors = models.IntegerField( null=True)
    image = models.ImageField(null=True, blank=False, upload_to="images/")
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.marque + " " + self.modele + " " + self.type


class Employee(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, null=True)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, null=True)
    nom = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.nom + " " + self.username + " " + self.role


class Contract(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom + " " + self.prenom


class Reservation(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, null=True)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, null=True)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    prix = models.FloatField()

    def __str__(self):
        return self.dateDebut + " " + self.dateFin + " " + self.prix


class Client(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True)
    facture = models.OneToOneField(Facture, on_delete=models.CASCADE, null=True)
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, null=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.nom + " " + self.prenom + " " + self.email + " " + self.username


class Agence(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)



class Sauce(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Sandwich(models.Model):
    name = models.CharField(max_length=100)
    sauces = models.ManyToManyField(Sauce, through='SauceQuantity')

    def _str_(self):
        return self.name

class SauceQuantity(models.Model):
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    sandwich = models.ForeignKey(Sandwich, on_delete=models.CASCADE)
    extra_sauce = models.BooleanField(default=False)

    def _str_(self):
        return "{}{}".format(self.sandwich.__str(), self.sauce.__str_())
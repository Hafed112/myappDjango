from django.db import models

# Create your models here.

class Filiere(models.Model):
    filiereNom=models.CharField(max_length=100)

    def __str__(self):
        return self.filiereNom




class Stagiaire(models.Model):
    fullName=models.CharField(max_length=100)
    stgMatricule=models.CharField(max_length=4)
    mobile=models.CharField(max_length=10)
    filiere=models.ForeignKey(Filiere,on_delete=models.CASCADE)
    
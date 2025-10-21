from django.db import models

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    nationalite = models.CharField(max_length=50)
    niveau_etudes = models.CharField(max_length=50)
    etablissement = models.CharField(max_length=100)
    annee_diplome = models.IntegerField()
    mention = models.CharField(max_length=50, blank=True)
    concours_choisi = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100, blank=True)
    extrait_naissance = models.FileField(upload_to='documents/')
    certificat = models.FileField(upload_to='documents/')
    lettre_motivation = models.FileField(upload_to='documents/')
    diplome = models.FileField(upload_to='documents/')
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenoms}"

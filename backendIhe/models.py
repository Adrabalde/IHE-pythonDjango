from django.db import models

# Create your models here.
class Auditeur(models.Model):
    id_auditeur = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='images/')
    nom_prenom = models.CharField(max_length=150)
    poste = models.CharField(max_length=150)
    annee_formation = models.CharField(max_length=10)
    avis = models.TextField()

    class Meta:
        managed = False # allow Django to create, modify and delete table Auditeur
        db_table = 'Auditeur'


class Evenement(models.Model):
    id_event = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=150)
    descriptif = models.TextField()
    date_event = models.DateField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        managed = False # allow Django to create, modify and delete table Evenement
        db_table = 'Evenement'


class Institut(models.Model):
    id_institut = models.AutoField(primary_key=True)
    sigle = models.CharField(max_length=150)
    nom_complet = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='images/')
    presentation = models.TextField()
    descriptif_formation = models.TextField()
    website = models.URLField(max_length=255)
    social_media = models.URLField(max_length=255,blank=True, null=True)

    class Meta:
        managed = False # allow Django to create, modify and delete table Institut
        db_table = 'Institut'


class Accueil(models.Model):
    id_accueil = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    sous_titre = models.CharField(max_length=100)
    texte = models.TextField()
    image = models.ImageField(upload_to='images/') 

    class Meta:
        managed = False # allow Django to create, modify and delete table Accueil
        db_table = 'Accueil'


class Experience(models.Model):
    id_experience = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=75)
    texte = models.TextField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        managed = False # allow Django to create, modify and delete table Experience
        db_table = 'Experience'


class Pedagogie(models.Model):
    id_pedagogie = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    sous_titre = models.CharField(max_length=100)
    texte = models.TextField()

    class Meta:
        managed = False # allow Django to create, modify and delete table Pedagogie 
        db_table = 'Pedagogie'


class AutreTexte(models.Model):
    id_autre = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    sous_titre = models.CharField(max_length=100)

    class Meta:
        managed = False # allow Django to create, modify and delete table Autretexte
        db_table = 'AutreTexte'
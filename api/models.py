from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Result(models.Model):
    board = models.CharField(max_length=255)
    roll = models.IntegerField()
    gpa = models.IntegerField()

    def __str__(self):
        return str(self.roll)


class Projet(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField(default=False)
    image = models.ImageField(upload_to='projet', null=True, blank=True)
 
def __str__(self):
        return self.libelle +","+self.description +","+str(self.date_debut)+","+self.type +","+str(self.date_fin)+","+self.acheve

class Service(models.Model):
    TYPE_CHOICES = (
        ('CG', 'Charte graphique'),
        ('O3D', 'Objet 3D'),
        ('SC', 'Scénarisation'),
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    description = models.TextField()
    def __str__(self):
        return self.description +","+self.type

class Details(models.Model):
    fichier = models.FileField(upload_to='details')
    Service = models.ForeignKey(Service, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)

def __str__(self):
        return self.fichier+","+self.Service +","+self.Projet



class Personnel(models.Model):
    name = models.CharField(max_length=100)
    fichier_cv = models.FileField(upload_to='cv')
    image = models.ImageField(upload_to='personnel', null=True, blank=True)
    lien_linkedin = models.URLField(null=True, blank=True)
def __str__(self):
        return self.name +","+self.fichier_cv +","+str(self.image)+","+self.lien_linkedin
class Equipe(models.Model):
    nom = models.CharField(max_length=255)
    members = models.ManyToManyField(Personnel)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='equipe', null=True, blank=True)
   
    def __str__(self):
        return self.nom +","+str(self.projet)
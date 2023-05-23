from django.db import models

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
class Article(models.Model):
   
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
   
    def __str__(self):
        return self.titre 



class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.user.username
    @receiver(post_save, sender=User)
    def create_client(sender, instance, created, **kwargs):
      if created:
          client = Clients.objects.create(user=instance, address="", phone_number="")
          print(f"Created client {client.pk} for user {instance.username}")

class Services(models.Model):
    TYPE_CHOICES = [
        ('Design Graphique', 'Design Graphique'),
        ('Design Web', 'Design Web'),
        ('SC', 'Scénarisation'),
    ]
    
    nom = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ImageField( null=True, blank=True)
   
    def __str__(self):
        return self.nom



    
class DemandeProjet(models.Model):
    libelle = models.CharField(max_length=50)
    description = models.TextField()
    date_demande = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey('Clients', on_delete=models.CASCADE, null=True, blank=True)
    STATUT_CHOICES = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé')
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    
    def __str__(self):
        return self.libelle
    
    
class Equipes(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image= models.ImageField( blank=True)
   
    
    def __str__(self):
        return self.nom



class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    formations = models.ManyToManyField('Formation', related_name='paniers')
    date_ajout = models.DateTimeField(default=timezone.now)    
    quantite = models.IntegerField(default=1)
    def total_prix(self):
        return sum([f.prix for f in self.formations.all() if f.prix])



class Formation(models.Model):
    nom = models.CharField(max_length=255)
    photo = models.ImageField()
    description = models.TextField()
    datedebut = models.DateField()
    datefin = models.DateField()
    nbheure_semaine = models.IntegerField()
    prix = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    formateur = models.ForeignKey('Formateur', on_delete=models.CASCADE,null=True, blank=True)
    lienmeet = models.URLField()
    service = models.ForeignKey('Services', on_delete=models.CASCADE ,null=True, blank=True)
    
    def __str__(self):
        return self.nom
    

class Formateur(models.Model):
    fullname = models.CharField(max_length=255)
    photo = models.ImageField(null=True, blank=True)
    DOMAIN_CHOICES = (
        ('DG', 'Design Graphique'),
        ('DW', 'Design Web'),
        ('SC', 'Scénarisation'),
    )
    domaine = models.CharField(max_length=2, choices=DOMAIN_CHOICES)
    rating = models.FloatField()

    def __str__(self):
        return self.fullname


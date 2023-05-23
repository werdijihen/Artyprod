from django.db import models

class Projett(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    acheve = models.BooleanField(default=False)
    image = models.ImageField(upload_to='projet', null=True, blank=True)
 
def __str__(self):
        return self.libelle +","+self.description +","+str(self.date_debut)+","+self.type +","+str(self.date_fin)+","+self.acheve
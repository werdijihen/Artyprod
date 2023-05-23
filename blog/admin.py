from django.contrib import admin
from .models import *
# Register your models here.
from .models import Article
admin.site.register(Article)
from .models import Clients
admin.site.register(Clients)
from .models import DemandeProjet
admin.site.register(DemandeProjet)
from .models import Services
admin.site.register(Services)
from .models import Formateur
admin.site.register(Formateur)
from .models import Formation
admin.site.register(Formation)
from .models import Equipes
admin.site.register(Equipes)

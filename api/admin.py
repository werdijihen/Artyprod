from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Result)
from .models import Service
admin.site.register(Service)
from .models import Projet
admin.site.register(Projet)
from .models import Details
admin.site.register(Details)
from .models import Equipe
admin.site.register(Equipe)
from .models import Personnel
admin.site.register(Personnel)

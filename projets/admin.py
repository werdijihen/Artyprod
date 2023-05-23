from django.contrib import admin
from .models import *

# Register your models here.
from .models import Projet
admin.site.register(Projet)
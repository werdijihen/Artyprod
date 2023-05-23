from django.contrib import admin
from .models import OfficialInfo, PersonalInfo
from .models import *
# Register your models here.
admin.site.register(OfficialInfo)
admin.site.register(PersonalInfo)

from .models import Service
admin.site.register(Service)
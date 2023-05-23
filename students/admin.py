from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StudentClassInfo)
admin.site.register(StudentSectionInfo)
admin.site.register(StudentShiftInfo)
admin.site.register(StudentInfo)

from .models import Projet
admin.site.register(Projet)
from .models import Equipe
admin.site.register(Equipe)
from .models import ProjectView
admin.site.register(ProjectView)
from .models import Client
admin.site.register(Client)
from .models import ProjectRequest
admin.site.register(ProjectRequest)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'status', 'date']
admin.site.register(Attendance, AttendanceAdmin)


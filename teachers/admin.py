from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TeacherDeptInfo)
admin.site.register(TeacherSubInfo)
admin.site.register(TeacherInfo)

from .models import Personnel
admin.site.register(Personnel)
from .models import PaymentHistory
admin.site.register(PaymentHistory)
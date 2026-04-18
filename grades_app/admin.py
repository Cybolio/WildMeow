from django.contrib import admin
from .models import Grade, DemandReport, Prerequisite

admin.site.register(Grade)
admin.site.register(DemandReport)
admin.site.register(Prerequisite)
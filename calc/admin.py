from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Nighty, Inskirt, Blouse, Saree) 
class viewadmin(ImportExportModelAdmin):
    pass
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from admins.models import Account
from users.models import patient, approved, centre, medicine


@admin.register(patient,approved,centre,Account,medicine)
class ViewAdmin(ImportExportModelAdmin):
    search_fields = ['dylnumber','otp','centre']
    pass
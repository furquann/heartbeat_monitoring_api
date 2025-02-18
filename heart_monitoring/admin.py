from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Patient, HeartRateRecord

# Register the custom User model
admin.site.register(get_user_model())


# Registering Patient model
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'contact_number')
    list_filter = ('gender', 'created_at')

# Registering HeartRateRecord model
@admin.register(HeartRateRecord)
class HeartRateRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'heart_rate', 'recorded_at', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name')
    list_filter = ('recorded_at',)
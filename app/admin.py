from django.contrib import admin
from .models import Caregiver, Patient, Medication, HealthMetric, Appointment

admin.site.register(Caregiver)
admin.site.register(Patient)
admin.site.register(Medication)
admin.site.register(HealthMetric)
admin.site.register(Appointment)

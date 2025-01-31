from django.db import models
from django.urls import reverse



class Caregiver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField(blank=True, null=True)
    primary_caregiver = models.ForeignKey(
        Caregiver,
        on_delete=models.SET_NULL,
        related_name='patients',
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse('patient_detail',args=[str(self.id)])


class Medication(models.Model):
    name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, null=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='medications'
    )

    def __str__(self):
        return f"{self.name} ({self.dosage}) - {self.patient}"


class HealthMetric(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='health_metrics'
    )
    metric_type = models.CharField(max_length=100)  # e.g., "Blood Pressure", "Heart Rate"
    value = models.CharField(max_length=50)
    measured_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_type} - {self.value} ({self.patient})"


class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateTimeField()
    description = models.TextField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.patient} on {self.appointment_date} - Resolved: {self.resolved}"


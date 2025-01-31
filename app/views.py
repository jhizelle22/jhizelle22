from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, Caregiver, Medication, HealthMetric, Appointment
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView

class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log the user in after signup
        return redirect('login') 

class LoginPageView(TemplateView):
    template_name = 'app/login.html'

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class SignupPageView(TemplateView):
    template_name = 'app/signup.html'

class CaregiverListView(ListView):
    model = Caregiver
    template_name = 'caregiver_list.html'
    context_object_name = 'caregivers'  

class CaregiverDetailView(DetailView):
    model = Caregiver
    template_name = 'app/caregiver_detail.html'

class CaregiverCreateView(CreateView):
    model = Caregiver
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    template_name = 'app/caregiver_create.html'
    success_url = reverse_lazy('caregiver_list')  

class CaregiverUpdateView(UpdateView):
    model = Caregiver
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    template_name = 'app/caregiver_update.html'
    success_url = reverse_lazy('caregiver_list')  

class CaregiverDeleteView(DeleteView):
    model = Caregiver
    template_name = 'app/caregiver_delete.html'
    success_url = reverse_lazy('caregiver_list')  


class PatientListView(ListView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'app/patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'app/patient_detail.html'

class PatientCreateView(CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'address', 'primary_caregiver']
    template_name = 'app/patient_create.html'

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'address', 'primary_caregiver']
    template_name = 'app/patient_update.html'

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'app/patient_delete.html'
    success_url = reverse_lazy('patient_list')

class MedicationListView(ListView):
    model = Medication
    template_name = 'app/medication_list.html'
    context_object_name = 'medications'

class MedicationDetailView(DetailView):
    model = Medication
    template_name = 'app/medication_detail.html'

class MedicationCreateView(CreateView):
    model = Medication
    fields = ['name', 'dosage', 'instructions', 'patient']
    template_name = 'app/medication_create.html'
    success_url = reverse_lazy('medication_list')

class MedicationUpdateView(UpdateView):
    model = Medication
    fields = ['name', 'dosage', 'instructions', 'patient']
    template_name = 'app/medication_update.html'
    success_url = reverse_lazy('medication_list')

class MedicationDeleteView(DeleteView):
    model = Medication
    template_name = 'app/medication_delete.html'
    success_url = reverse_lazy('medication_list')

class HealthMetricListView(ListView):
    model = HealthMetric
    template_name = 'app/healthmetric_list.html'
    context_object_name = 'health_metrics'

class HealthMetricDetailView(DetailView):
    model = HealthMetric
    template_name = 'app/healthmetric_detail.html'
    context_object_name = 'health_metric'

class HealthMetricCreateView(CreateView):
    model = HealthMetric
    fields = ['patient', 'metric_type', 'value']
    template_name = 'app/healthmetric_create.html'
    success_url = reverse_lazy('healthmetric_list')

class HealthMetricUpdateView(UpdateView):
    model = HealthMetric
    fields = ['patient', 'metric_type', 'value']
    template_name = 'app/healthmetric_update.html'
    success_url = reverse_lazy('healthmetric_list')

class HealthMetricDeleteView(DeleteView):
    model = HealthMetric
    template_name = 'app/healthmetric_delete.html'
    success_url = reverse_lazy('healthmetric_list')

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'app/appointment_list.html'
    context_object_name = 'appointments'

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'app/appointment_detail.html'
    context_object_name = 'appointment'

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['patient', 'appointment_date', 'description', 'resolved' ]
    template_name = 'app/appointment_create.html'
    success_url = reverse_lazy('appointment_list')  # Redirect to the appointment list after creation

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['patient', 'appointment_date', 'description', 'resolved' ]
    template_name = 'app/appointment_update.html'
    success_url = reverse_lazy('appointment_list')  # Redirect to the appointment list after update

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'app/appointment_delete.html'
    success_url = reverse_lazy('appointment_list')  # Redirect to the appointment list after deletion




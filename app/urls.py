from django.contrib.admin.templatetags.admin_list import pagination_tag
from django.shortcuts import redirect
from django.urls import path
from .views import HomePageView, AboutPageView,  SignupPageView
from .views import SignupView
from .views import (
    CaregiverListView, 
    CaregiverDetailView, 
    CaregiverCreateView, 
    CaregiverUpdateView, 
    CaregiverDeleteView, 
    PatientListView, 
    PatientDetailView, 
    PatientCreateView,
    PatientUpdateView,
    PatientDeleteView,
     MedicationListView, 
    MedicationDetailView, 
    MedicationCreateView, 
    MedicationUpdateView, 
    MedicationDeleteView,
    HealthMetricListView, 
    HealthMetricDetailView, 
    HealthMetricCreateView, 
    HealthMetricUpdateView, 
    HealthMetricDeleteView,
    AppointmentListView,
    AppointmentDetailView,
    AppointmentCreateView,  
    AppointmentUpdateView,
    AppointmentDeleteView,
    

)

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('', lambda request: redirect('login')),
    path('', HomePageView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('about/', AboutPageView.as_view(), name='about'),
    

    path('caregivers/', CaregiverListView.as_view(), name='caregiver_list'),
    path('caregivers/<int:pk>/', CaregiverDetailView.as_view(), name='caregiver_detail'),
    path('caregivers/create/', CaregiverCreateView.as_view(), name='caregiver_create'),
    path('caregivers/<int:pk>/edit/', CaregiverUpdateView.as_view(), name='caregiver_update'),
    path('caregivers/<int:pk>/delete/', CaregiverDeleteView.as_view(), name='caregiver_delete'),

    path('patients/', PatientListView.as_view(), name='patient'),    
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patients/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patients/update/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
    path('patients/delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
    path('patients/', PatientListView.as_view(), name='patient_list'), 

    path('medications/', MedicationListView.as_view(), name='medication_list'),
    path('medications/<int:pk>/', MedicationDetailView.as_view(), name='medication_detail'),
    path('medications/create/', MedicationCreateView.as_view(), name='medication_create'),
    path('medications/<int:pk>/edit/', MedicationUpdateView.as_view(), name='medication_update'),
    path('medications/<int:pk>/delete/', MedicationDeleteView.as_view(), name='medication_delete'),

    path('health-metrics/', HealthMetricListView.as_view(), name='healthmetric_list'),
    path('health-metrics/<int:pk>/', HealthMetricDetailView.as_view(), name='healthmetric_detail'),
    path('health-metrics/create/', HealthMetricCreateView.as_view(), name='healthmetric_create'),
    path('health-metrics/<int:pk>/edit/', HealthMetricUpdateView.as_view(), name='healthmetric_update'),
    path('health-metrics/<int:pk>/delete/', HealthMetricDeleteView.as_view(), name='healthmetric_delete'),

    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
    

    
]


from django.urls import path
from . import views

urlpatterns = [
    path('view_record/<int:patient_id>/', views.viewRecord, name='viewRecord'),
    path('display_test_report/<int:patient_id>/', views.displayTestReport, name='displayTestReport'),
    path('display_prescription/<int:patient_id>/', views.displayPrescription, name='displayPrescription'),
    path('display_long_term_record/<int:patient_id>/', views.displayLongTermRecords, name='displayLongTermRecords'),

]

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import LongTermRecord, TestReport, Prescription, PrescriptionMedicine, TestPrescription
from User.models import Patient
from django.shortcuts import HttpResponse
import json

def home(request):
    if(request.session.get('username') is not None):
        temp = "Home Page - Logged in as ", request.session.get("username")
        return HttpResponse(temp)
    return HttpResponse("Home Page - Login to Continue")

def viewRecord(request, patient_id):
    patient = Patient.objects.filter(patient_id=patient_id)
    if(patient.count() == 0):
        return HttpResponse("Invalid Patient ID")
    patient = patient[0]
    long_term_records = LongTermRecord.objects.filter(patient=patient).count()
    prescriptions = Prescription.objects.filter(patient=patient).count()
    test_reports = TestReport.objects.filter(patient=patient).count()
    print(long_term_records)
    print(prescriptions)
    print(test_reports)
    context = {
        "long_term_records":long_term_records,
        "prescriptions":prescriptions,
        "test_reports":test_reports
    }
    return render(request, 'Record/view_records.html', context)


def displayTestReport(request, test_report_id):
    test_reports = TestReport.objects.filter(test_report_id=test_report_id).values('test_report_id', 'patient_id', 'test_id', 'observations', 'date_conducted')
    context = {
        "test_reports":test_reports
    }
    return render(request, 'Record/view_records.html', context)


def displayPrescription(request, prescription_id):
    prescriptions = Prescription.objects.filter(prescription_id=prescription_id).values('prescription_id', 'patient_id', 'doctor_id', 'diagnosis', 'observations', 'notes')
    context = {
        "prescriptions":prescriptions
    }
    return render(request, 'Record/view_records.html', context)

def displayLongTermRecords(request, long_term_record_id):
    long_term_records = LongTermRecord.objects.filter(long_term_record_id=long_term_record_id).values('long_term_record_id', 'patient_id', 'date_of_entry', 'diagnosis', 'notes')
    context = {
        "long_term_records":long_term_records
    }
    return render(request, 'Record/view_records.html', context)
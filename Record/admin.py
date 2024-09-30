from django.contrib import admin
from .models import Prescription, PrescriptionMedicine, TestPrescription, TestReport, LongTermRecord

admin.site.register(Prescription)
admin.site.register(PrescriptionMedicine)
admin.site.register(TestPrescription)
admin.site.register(TestReport)
admin.site.register(LongTermRecord)

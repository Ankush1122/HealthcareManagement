from django.contrib import admin
from .models import User, Patient, Doctor, Nurse, Pharmacist, Pathologist, Admin, InsuranceCompany, LawEnforcementAgency, Hospital

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Pharmacist)
admin.site.register(Pathologist)
admin.site.register(Admin)
admin.site.register(InsuranceCompany)
admin.site.register(LawEnforcementAgency)
admin.site.register(Hospital)

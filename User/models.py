from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class User(models.Model):
    ROLES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Pharmacist', 'Pharmacist'),
        ('Pathologist', 'Pathologist'),
        ('Admin', 'Admin'),
        ('InsuranceAgent', 'Insurance Agent'),
        ('LawEnforcement', 'Law Enforcement'),
        ('Hospital', 'Hospital')
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLES)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)
    verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.username} ({self.role})"


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    insurance_policy_number = models.CharField(max_length=50)
    primary_physician = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Patient {self.user.username}"


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    hospital = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"


class Nurse(models.Model):
    nurse_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse_profile')
    supervising_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    hospital = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Nurse {self.user.username}"


class Pharmacist(models.Model):
    pharmacist_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pharmacist_profile')
    hospital = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Pharmacist {self.user.username}"


class Pathologist(models.Model):
    pathologist_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pathologist_profile')
    hospital = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Pathologist {self.user.username}"


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    admin_details = models.TextField()

    def __str__(self):
        return f"Admin {self.user.username}"


class InsuranceCompany(models.Model):
    insurance_company_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='insurance_company_profile')
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class LawEnforcementAgency(models.Model):
    agency_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='law_enforcement_profile')
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hospital_profile')
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
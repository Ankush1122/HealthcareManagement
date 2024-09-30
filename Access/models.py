from django.db import models
from User.models import Patient, User, Doctor, Admin, InsuranceCompany, LawEnforcementAgency
from Record.models import Prescription, TestReport, LongTermRecord


class AccessPermission(models.Model):
    PERMISSION_TYPES = [
        ('View', 'View'),
        ('Add', 'Add'),
        ('Modify', 'Modify')
    ]

    permission_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    granted = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_granted = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    permission_type = models.CharField(max_length=10, choices=PERMISSION_TYPES)

    def __str__(self):
        return f"Permission {self.permission_type} for {self.user} on {self.patient}"


class EmergencyAccessLog(models.Model):
    access_log_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_accessed = models.DateTimeField(auto_now_add=True)
    justification_submitted = models.BooleanField(default=False)
    justification_text = models.TextField(null=True, blank=True)
    admin_notified = models.BooleanField(default=False)
    patient_notified = models.BooleanField(default=False)

    def __str__(self):
        return f"Emergency Access by {self.doctor} for {self.patient}"


class RecordDeletionRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Disapproved', 'Disapproved')
    ]

    RECORD_TYPES = [
        ('Prescription', 'Prescription'),
        ('TestReport', 'TestReport'),
        ('LongTermRecord', 'LongTermRecord')
    ]

    deletion_request_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=20, choices=RECORD_TYPES)
    record_id = models.IntegerField()
    date_requested = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pending')
    reason = models.TextField()

    def __str__(self):
        return f"Record Deletion Request {self.deletion_request_id} for {self.patient}"


class InsuranceAccessRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Denied', 'Denied')
    ]

    request_id = models.AutoField(primary_key=True)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_approved = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Insurance Access Request {self.request_id} for {self.patient}"


class LegalAccessRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Denied', 'Denied')
    ]

    legal_request_id = models.AutoField(primary_key=True)
    agency = models.ForeignKey(LawEnforcementAgency, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    warrant_document = models.FileField(upload_to='warrants/', null=True, blank=True)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_approved = models.DateTimeField(null=True, blank=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Legal Access Request {self.legal_request_id} for {self.patient}"

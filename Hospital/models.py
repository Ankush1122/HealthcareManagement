from django.db import models
from User.models import User, Patient, Doctor, Pharmacist, Pathologist, Hospital

class Visit(models.Model):
    VISIT_TYPES = [
        ('Doctor', 'Doctor'),
        ('Pharmacist', 'Pharmacist'),
        ('Pathologist', 'Pathologist')
    ]

    visit_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_visit = models.DateTimeField()
    visit_type = models.CharField(max_length=20, choices=VISIT_TYPES)
    entity = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role__in': ['Doctor', 'Pharmacist', 'Pathologist']})
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    bill = models.ForeignKey('Bill', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Visit {self.visit_id} - {self.visit_type} for {self.patient}"

class Bill(models.Model):
    BILL_STATUS = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid')
    ]

    bill_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    entity = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role__in': ['Doctor', 'Pharmacist', 'Pathologist']})
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=BILL_STATUS, default='Unpaid')
    details = models.TextField()

    def __str__(self):
        return f"Bill {self.bill_id} - {self.status} for {self.patient}"

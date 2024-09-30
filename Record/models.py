from django.db import models
from User.models import Patient, Doctor, Pathologist
from Inventory.models import Tests, Medicines


class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(auto_now_add=True)
    diagnosis = models.CharField(max_length=255)
    observations = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return f"Prescription {self.prescription_id} for {self.patient}"


class PrescriptionMedicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = (('prescription', 'medicine'),)

    def __str__(self):
        return f"Medicine {self.medicine.name} for Prescription {self.prescription.prescription_id}"


class TestPrescription(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('test', 'prescription'),)

    def __str__(self):
        return f"Test {self.test.test_name} for Prescription {self.prescription.prescription_id}"


class TestReport(models.Model):
    test_report_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    pathologist = models.ForeignKey(Pathologist, on_delete=models.CASCADE)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    observations = models.TextField()
    date_conducted = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Test Report {self.test_report_id} for {self.patient}"


class LongTermRecord(models.Model):
    long_term_record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_entry = models.DateTimeField(auto_now_add=True)
    diagnosis = models.CharField(max_length=255)
    test_results = models.ForeignKey(TestReport, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return f"Long Term Record {self.long_term_record_id} for {self.patient}"

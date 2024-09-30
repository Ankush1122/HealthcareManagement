from django.db import models

class Tests(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=100)
    test_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.test_name} ({self.test_type})"

class Medicines(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.dosage}"

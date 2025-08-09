from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.speciality}"


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    appointment_date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def clean(self):
        if self.appointment_date < date.today():
            raise ValidationError("Appointment date cannot be in the past.")

    def __str__(self):
        return f"{self.patient_name} with {self.doctor.name} on {self.appointment_date}"

from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female' ,'Female')])
    specialization = models.CharField(max_length=100)
    days_available = models.CharField(max_length=100)# 'mon-fri'
    hours_per_day = models.IntegerField() #6
    
    def __str__(self):
        return f"Dr. {self.name} . {self.specialization}"
    
    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    doctor = models.ForeignKey(
        Doctor,
        on_delete= models.CASCADE,
        related_name='patients'
    )
    appointment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - Dr . {self.doctor.name}"
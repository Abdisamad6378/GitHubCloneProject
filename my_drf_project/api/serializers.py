from rest_framework import serializers
from.models import Task
from.models import Patient

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class Patientserializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'doctor', 'doctor_name', 'appointment_date']
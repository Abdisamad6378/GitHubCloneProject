from django.shortcuts import render
from rest_framework import viewsets
from.models import Task
from.serializers import Taskserializer
from .serializers import Patientserializer
from.models import Patient

# Create your views here.
class TaskViewSets(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class = Taskserializer
    
    
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = Patientserializer
from django.shortcuts import render
from django.views.generic import ListView
from .models import Doctor


class ListDoctor(ListView):
    model = Doctor
    template_name = "doctors/doctor_create.html"
    context_object_name = 'doctors'

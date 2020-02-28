from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Doctor
from .forms import DoctorForms


class ListDoctor(ListView):
    model = Doctor
    context_object_name = 'doctors'



class DoctorUpdate(UpdateView):
    model = Doctor
    form_class = DoctorForms
    success_url = "doctors/doctor_list.html"


class DoctorDelete(DeleteView):
    def get(self, request, pk):
        doctor = Doctor.objects.get(pk=pk)
        doctor.delete()
        return redirect(reverse_lazy('list'))



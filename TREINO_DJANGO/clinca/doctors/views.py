from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Doctor
from .forms import DoctorForms


class ListDoctor(ListView):
    model = Doctor
    context_object_name = 'doctors'


class CreateDoctor(CreateView):
    model = Doctor
    form_class = DoctorForms
    template_name = "doctors/doctor_form.html"
    success_url = "doctors/doctor_list.html"


class DoctorUpdate(UpdateView):
    model = Doctor
    form_class = DoctorForms
    success_url = "doctors/doctor_list.html"


class DoctorDelete(DeleteView):
    def get(self, request, pk):
        doctor = Doctor.objects.get(pk=pk)
        doctor.delete()
        return render("doctors/doctor_list.html")



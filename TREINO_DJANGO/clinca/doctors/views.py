from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView
from .models import Doctor
from .forms import DoctorForms


class ListDoctor(TemplateView):
    template_name = 'doctors/doctor_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()
        context['form'] = DoctorForms(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form']
        if form.is_valid():
            form.save()
            redirect(reverse_lazy('list'))


class DoctorUpdate(UpdateView):
    model = Doctor
    form_class = DoctorForms
    success_url = "doctors/doctor_list.html"


class DoctorDelete(DeleteView):
    def get(self, request, pk):
        doctor = Doctor.objects.get(pk=pk)
        doctor.delete()
        return redirect(reverse_lazy('list'))



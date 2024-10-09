from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, CreateView, UpdateView, View
from app.models import Employee
from app.forms import EmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy


# Create your views here.
class EmployeeListView(ListView):
    model = Employee
    template_name = "employeeList.html"
    context_object_name = "employees"


class CreateEmployee(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = "createEmployee.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("listView")


class UpdateEmployee(LoginRequiredMixin, UpdateView):
    model = Employee
    template_name = "createEmployee.html"
    form_class = EmployeeForm

    def get_success_url(self):
        return reverse_lazy('listView') 
    
class deleteEmployee(LoginRequiredMixin, View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk = pk)
        employee.delete()
        return redirect('listView')
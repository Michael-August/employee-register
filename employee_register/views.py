from employee_register.models import Employee
from employee_register.forms import EmployeeForm
from django.shortcuts import redirect, render

# Create your views here.

def employee_list(request):
    context = {'employee_list': Employee.objects.all}
    return render(request, 'employee_list.html', context)


def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render(request, 'employee_form.html', {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/list')


def employee_delete(request):
    pass

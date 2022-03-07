from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        label = {
            'fullname': 'Full Name',
            'emp_code': 'Emp code'
        }

    # Making the initial drop down to show as Select
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'select'
        # Excluding validation on some fields
        self.fields['emp_code'].required = False

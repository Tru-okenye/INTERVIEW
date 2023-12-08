from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    position = forms.ModelChoiceField(queryset=Position.objects.all(), empty_label="Select Position")
    class Meta:
        model = Employee
        fields= '__all__'

   

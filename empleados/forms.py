from django import forms 

class EmployeeFilterForm(forms.Form):
    businessentityid = forms.CharField(max_length=1, required=False)
    jobtitle = forms.CharField(max_length=50, required=False)
    gender = forms.CharField(max_length=10, required=False)
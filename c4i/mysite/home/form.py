from django import forms
from .models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name', 'found_date', 'location']

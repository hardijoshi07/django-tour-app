from django import forms
from .models import TourPackage

class TourPackageForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = '__all__'

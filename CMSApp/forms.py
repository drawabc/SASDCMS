from django.forms import ModelForm

from .models import CivilianData

class CivilianForm(ModelForm):
    class Meta:
        model = CivilianData
        fields = ['nric', 'name', 'mobile', 'email']


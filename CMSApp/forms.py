from django.forms import ModelForm

from .models import CivilianData


class AddCivilianForm(ModelForm):
    class Meta:
        model = CivilianData
        fields = ['nric', 'name', 'mobile', 'email']

class EditCivilianForm(ModelForm):
    class Meta:
        model = CivilianData
        fields = ['nric', 'name', 'mobile', 'email', 'region']

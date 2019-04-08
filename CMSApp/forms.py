from django.forms import ModelForm
from django import forms

from .models import CivilianData

REGIONS = [('NORTH-EAST','NORTH-EAST'), ('NORTH', 'NORTH'), ('WEST', 'WEST'), ('EAST', 'EAST'), ('CENTRAL', 'CENTRAL')]

class CivilianForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CivilianForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['region'] = forms.ChoiceField(choices=REGIONS)
    class Meta:
        model = CivilianData
        fields = '__all__'


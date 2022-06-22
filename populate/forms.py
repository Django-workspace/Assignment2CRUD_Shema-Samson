from django import forms
from .models import retrievedata

class traineeforms(forms.ModelForm):
    class Meta:
        model=retrievedata
        fields="__all__"
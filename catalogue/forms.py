from django import forms
from catalogue.models import Representation

class RepresentationForm(forms.ModelForm):
    schedule = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Representation
        fields = ['spectacle', 'schedule', 'location']

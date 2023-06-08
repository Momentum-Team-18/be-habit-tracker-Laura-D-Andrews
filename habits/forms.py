from django import forms
from .models import Tracker, Record


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ('goal',)


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('date', 'goal_met', 'record_number')

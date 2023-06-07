from django import forms
from .models import Tracker


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ('goal',)


class RecordForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ('date', 'goal_met')

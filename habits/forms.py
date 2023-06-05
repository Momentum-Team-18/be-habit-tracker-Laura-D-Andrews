from django import forms
from .models import User, Tracker


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ('category', 'name', 'number_days_week',
                  'times_a_day', 'length_in_minutes')

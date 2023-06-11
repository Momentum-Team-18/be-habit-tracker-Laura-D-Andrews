from django import forms
from .models import Tracker, Record, Profile


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ('goal',)


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('date', 'goal_met', 'record_number')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthdate', 'occupation', 'postcode')


class FollowerForm(forms.ModelForm):
    class Meta:
        pass

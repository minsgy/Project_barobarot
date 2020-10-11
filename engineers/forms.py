import datetime as dt
from django import forms
from . models import Schedule

HOUR_CHOICES = [(dt.time(hour=x, minute=0), '{:02d}:00'.format(x)) for x in range(0, 24)]

class MyForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['scheduled_time']
        widgets = {'scheduled_time': forms.Select(choices=HOUR_CHOICES)}
        
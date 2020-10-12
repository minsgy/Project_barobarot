import datetime as dt
from django import forms
from . models import Schedule

HOUR_CHOICES = [(dt.time(hour=x ), '{:02d}:00'.format(x)) for x in range(0, 24)]

class MyForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['scheduled_time']
        widgets = {'scheduled_time': forms.Select(choices=HOUR_CHOICES) }   #시간 동적 선택

        # def __init__(self, *args, **kwargs):
        #     super(MyForm, self).__init__(*args, **kwargs)
        #     self.fields['scheduled_time'].choices = HOUR_CHOICES
        

        # forms.Select(choices=HOUR_CHOICES)
        
        
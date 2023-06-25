from django import forms
from .models import Conference
from .models import Session

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['title', 'date', 'category', 'venue', 'theme']


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'start_time', 'end_time', 'speakers']
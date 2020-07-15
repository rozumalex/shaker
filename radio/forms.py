from django import forms
from django.forms.widgets import HiddenInput

from .models import Track
from django.http import request


class TrackUploadForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = ['file']

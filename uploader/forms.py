from django import forms
from .models import photos
import datetime
from django.core.exceptions import ValidationError

class ImageForm(forms.ModelForm):
 class Meta:
  model = photos
  fields = {'title', 'image'}
  labels = {'photo':''}
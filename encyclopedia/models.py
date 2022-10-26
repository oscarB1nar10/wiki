from django.db import models
from django import forms
# Create your models here.

class NewPageForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(label="content")

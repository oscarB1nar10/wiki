from cProfile import label
from logging import PlaceHolder
from tkinter import Widget
from django.db import models
from django import forms
# Create your models here.


class NewPageForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'name': 'title', 'placeholder': 'title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'name': 'content', 'placeholder': 'Content'}))


from rest_framework import serializers
from django import forms

from .models import Project


def validate_name(value):
    qs = Project.objects.filter(name__iexact=value)
    if qs.exists():
        raise forms.ValidationError("This project has already been entered into the database.")
    return value


def validate_abb(value):
    qs = Project.objects.filter(abbreviation__iexact=value)
    if qs.exists():
        raise forms.ValidationError("This abbreviation is being use by another project.")
    return value
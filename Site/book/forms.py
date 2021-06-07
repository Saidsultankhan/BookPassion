from django import forms
from django.db.models import fields

from .models import Reviews

class ReviewForm(forms.ModelForm):

    class Meta:

        model = Reviews
        fields = ('name', 'email', 'text')
from django import forms
from ddfleetapp.models import Fleet

from .models import Card

class CardNumber(forms.Form):
    a_card = forms.IntegerField(label=Card.name, min_value=1)


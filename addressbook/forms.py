from django import forms
from .models import Person


class CreatePersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            "name",
            "surname",
            "address",
            'phone_number',
            "url",
            "image",
        ]

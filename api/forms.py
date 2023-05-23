






from django import forms

from .models import Equipe


class EquipForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = "__all__" 
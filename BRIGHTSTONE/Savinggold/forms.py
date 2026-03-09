from django import forms
from .models import Saver

class SaverForm(forms.ModelForm):
    class Meta:
        model = Saver
        fields = ['first_name','last_name','phone']
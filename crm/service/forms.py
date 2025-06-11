from django import forms
from .models import Service
from user.models import User

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['meal', 'served_by', 'portion_count']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['served_by'].queryset = User.objects.filter(role='chef')

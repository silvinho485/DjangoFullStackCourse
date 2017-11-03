from django import forms
from AppTwo.models import WebUsers

class NewUserForm(forms.ModelForm):
    class Meta():
        model = WebUsers
        fields = '__all__'
        # exclude = ['img']

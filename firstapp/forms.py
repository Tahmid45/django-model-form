from django import forms
from firstapp.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name','roll']
        # exclude = ['roll']
        labels = {
            'name':'Student Name',
            'roll':'Student Roll'
        }

        widgets = {
            'name': forms.TextInput()
        }
        help_texts = {
            'name':"write your full name",
            'roll' : "please write your roll"
        }
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }

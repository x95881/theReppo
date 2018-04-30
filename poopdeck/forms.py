from django import forms
from .models import Events






class eventForm(forms.ModelForm):
	description = forms.CharField(label='description', max_length=100)
	duration = forms.CharField(label='duration', max_length=30)
	importance = forms.CharField(label='importance', max_length=30)
	location = forms.CharField(label='location', max_length=30)
	completionStatus = forms.CharField(label='completion status', max_length=3)
	class Meta:
		model = Events
		fields = '__all__'


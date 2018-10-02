from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from mainApp.models import MainView

class MainViewForm(forms.ModelForm):
	service = forms.CharField(widget = forms.TextInput(
		attrs = {
		'class':'form-control'
		}))
	author = forms.CharField(widget = forms.TextInput(
		attrs = {
		'class':'form-control'
		}))
	description = forms.CharField(widget = forms.TextInput(
		attrs = {
		'class':'form-control'
		}))


	class Meta:
		model = MainView
		fields = ('photo', 'service', 'author', 'description', 'access', 'keywords', )

from django import forms

class ThreadForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)


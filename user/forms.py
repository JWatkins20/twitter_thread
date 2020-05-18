from django import forms

class ThreadForm(forms.Form):
	text = forms.CharField(
		widget=forms.Textarea(attrs={
			'cols': 150,
			'rows': 20,
			'class' : 'col-xs-12'
		}),
		label="",
		help_text=""
	)


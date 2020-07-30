from django import forms
from .models import Thread

class ThreadForm(forms.ModelForm):

	text = forms.CharField(
		widget=forms.Textarea(attrs={
				'placeholder': 'Some text',
				'cols': 150,
				'rows': 20,
				'class' : 'col-xs-12'
			}),
		label="",
		help_text="",
		initial=''
	)

	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Some title'}), label='')
	def __init__(self, *args, **kwargs):
		text = kwargs.pop('text', None)
		super(ThreadForm, self).__init__(*args, **kwargs)
		if text:
			self.fields['text'].initial = text
	
	class Meta:
		model = Thread
		fields = ('title', 'text')



from django import forms
from .models import Test1Model


# creating a form
class Test1Form(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Test1Model

		# specify fields to be used
		fields = [
			"title",
			"description",
		]

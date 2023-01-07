from django.forms import ModelForm
from .models import Links
class UserForm(ModelForm):
	class Meta:
		model = Links
		fields = ['link']
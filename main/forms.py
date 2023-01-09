from django.forms import ModelForm, FileInput
from .models import Links
class UserForm(ModelForm):
	class Meta:
		model = Links
		fields = ['link']
  
		widgets = {
      	"link": FileInput(attrs={
           "class": 'form-control',
           "id":"chooseFile"
           }),}
			
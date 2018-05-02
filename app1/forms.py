from django import forms
from models import VM
class VMForm(forms.ModelForm):
	class Meta:
		model = VM
		fields = ['name','harddisk','ram','cpu_cores','instance']
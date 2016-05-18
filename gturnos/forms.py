from django import forms
from .models import *
from django.forms import  TextInput

class OrganizacionForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Organizacion
		fields = ('nombre','domicilio','telefono')
		widgets = {
		'nombre': TextInput(attrs={'class':'form-control'}),
		'domicilio': TextInput(attrs={'class':'form-control'}),
		'telefono': TextInput(attrs={'class':'form-control'}),
		}
		
class PacienteForm(forms.ModelForm):
	"""docstring for PacienteForm"""
	class Meta:
		model = Paciente
		fields = ['apellido','nombres','dni','fecha_nac','altura','peso','perimetro_enc','domicilio','telefono','sexo','fecha_inicio']
		# widgets = {
		# 'apellido': TextInput(attrs={'class':'form-control'}),
		# 'nombres': TextInput(attrs={'class':'form-control'}),
		# #'fecha_nac':forms.DateInput(attrs={'class':'datepicker'}),
		# 'fecha_nac': DateWidget(attrs={'id':"fecha_nac"}, bootstrap_version=3),
		# #'fecha_nac': TextInput(attrs={'class':'form-control'}),
		# 'domicilio': TextInput(attrs={'class':'form-control'}),
		# 'telefono': TextInput(attrs={'class':'form-control'}),
		# 'dni': TextInput(attrs={'class':'form-control'}),
		# 'sexo': TextInput(attrs={'class':'form-control'}),
		# 'fecha_inicio':forms.DateInput(attrs={'class':'datepicker'}),	
		# #'fecha_inicio': DateWidget(attrs={'id':"fecha_nac",'class':'form-control'},usel10n = True, bootstrap_version=3	),	
		# 'altura': TextInput(attrs={'class':'form-control'}),
		# 'peso': TextInput(attrs={'class':'form-control'}),
		# 'perimetro_enc': TextInput(attrs={'class':'form-control'}),
		# }
		
class MedicoForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Medico
		fields = ['apellido','nombres','dni','fecha_nac','domicilio','telefono','sexo','mat_profesional']
		# widgets = {
		# 'apellido': TextInput(attrs={'class':'form-control'}),
		# 'nombres': TextInput(attrs={'class':'form-control'}),
		# 'fecha_nac': DateWidget(attrs={'id':"fecha_nac",'class':'form-control'},usel10n = True, bootstrap_version=3	),
		# 'domicilio': TextInput(attrs={'class':'form-control'}),
		# 'telefono': TextInput(attrs={'class':'form-control'}),
		# 'dni': TextInput(attrs={'class':'form-control'}),
		# 'sexo': TextInput(attrs={'class':'form-control'}),
		# 'mat_profesional': TextInput(attrs={'class':'form-control'}),
		# }

class HistoriaForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Historia_medica
		diagnostico=forms.CharField(widget=forms.Textarea)
		fields = ['fecha_historia','diagnostico','tratamiento','paciente','medico']
		# widgets = {
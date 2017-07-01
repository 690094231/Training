from django import  forms
from django.forms import ModelForm
from .models import Student,Course,Department
import re
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
	def clean_student_ID(self):
		student_ID = self.cleaned_data['student_ID']
		if re.match('^2015[0-9]{6}$',student_ID):
			return student_ID
		else:
			raise forms.ValidationError("Wrong Student Number")


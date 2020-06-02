from django import forms
from .models import *

class FirstcarouselForm(forms.Modelform):
	class Meta:
		model=Firstcarousel
		fields=['name','1.jpg']
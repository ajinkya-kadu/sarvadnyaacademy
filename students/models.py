from django.db import models

# Create your models here.
#to update photo on carousel slides on index page
	
class Pdfupload(models.Model):
	image=models.FileField(upload_to="students/pdffiles",default=" ")
	
class Admissions(models.Model):
	name=models.CharField(max_length=200,null=True)
	address=models.TextField(null=True)
	mobnum=models.IntegerField(null=True)
	parentmobnum=models.IntegerField(default=None,blank=True,null=True)
	course=models.TextField(default=None,blank=True,null=True)
	
	#def __str__(self):
	#	return self.firstname
	
	




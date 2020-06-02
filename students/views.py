#student app views

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pdfupload
from .models import Admissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login


def index(request):
	#firstcarousel=Firstcarousel.objects.all()
	return render(request,'index.html')
	
def about(request):
	return render(request,'about.html')
	
def ourresult(request):
	return render(request,'ourresult.html')

def admissions(request):
	if request.method=="POST":
		name=request.POST.get('name')
		address=request.POST.get('address')
		mobnum=request.POST.get('mobnum')
		parentmobnum=request.POST.get('parentmobnum')
		course=request.POST.get('course')
		admissions=Admissions(name=name,address=address,mobnum=mobnum,parentmobnum=parentmobnum,course=course)
		admissions.save()
	return render(request,'admissions.html')
	

def loginuser(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("/sarvid")
		else:
			messages.info(request,'Please enter correct Username or Password')
			return render(request,'login.html')
		
	return render(request,'login.html')
	
def logoutuser(request):
	logout(request)
	return render(request,'index.html')

def sarvid(request):
	print(request.user)
	if request.user. is_anonymous:
		return redirect("/login")
	return render(request,'sarvid.html')

def contactus(request):
	return render(request,'contactus.html')

def download(request):
	return render(request,'download.html')

def testseries(request):
	return render(request,'testseries.html')

def examtimetable(request):
	return render(request,'examtimetable.html')

# Create your views here.

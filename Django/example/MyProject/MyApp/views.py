import sys
from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

def Hello(request):
	return HttpResponse("Hello, world!")

def Hello2(request):
	IP = request.META['REMOTE_ADDR']  
	return render(request,'MyApp/Hello.html',{'content':"Hello,{0}".format(IP)})

def Hello3(request):
	return HttpRsponse("Hello,world3")

def signup(request):
	if request.method == 'POST':
		form = StudentForm(data = request.POST)
		if form.is_valid():
			new_student = form.save(commit = False)
			new_student.save()
			return HttpResponse("学生登陆成功")
	else:
		form = StudentForm()
	return render(request,'MyApp/signup.html',{'form':form})



# Create your views here.

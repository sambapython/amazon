# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import VM
from forms import VMForm

# Create your views here.
def home(request):
	data = VM.objects.all()
	return render(request,"home.html",{"data":data})
def createvm(request):
	msg = ""
	if request.method=="POST":
		import pdb; pdb.set_trace()
		form=VMForm(request.POST)
		form.save()
		msg="vm created successfully"
		return redirect("/home/")
	else:
		form=VMForm()
		return render(request,"createvm.html",{"vm_form":form, "msg":msg})
	
	

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
from .models import *
from django.contrib import messages

def index(request):
	# courses = Course.objects.all()
	# print courses
	return render(request, 'courses_new_app/index.html', {'courses': Course.objects.all()})

def add_course(request):
	if request.method == 'POST':
		errors = Course.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect ('/')
		else:
			print "in add"
			print request.POST
			course = Course.objects.create(name = request.POST['name'], description = request.POST['description'])
			course.save()
	return redirect('/')

def remove(request, id):
	return render(request, 'courses_new_app/destroy.html', {'course': Course.objects.get(id=id)})

def destroy(request, id):
	course = Course.objects.get(id=id)
	course.delete()
	return redirect('/')			

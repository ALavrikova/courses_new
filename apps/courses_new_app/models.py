# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):
    def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 1:
			errors['name'] = 'Name should be more than 1 character!'
		elif len(postData['description']) < 1:
			errors['description'] = 'Description should be longer than 1 character!'  
		return errors;

class Course(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	objects=CourseManager();  
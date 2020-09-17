#from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

# Create your models here.
#MVC MODEL VIEW CONTROLLER

def upload_location(instance, filename):
	# filebase, extension = filename.split(".")
	# return "%s/%s.%s" %(instance.id,instance.id, extension) 
	return "%s/%s" %(instance.id, filename) 

class Post(models.Model):
	title = models.CharField(max_length = 120)
	slug = models.SlugField(unique = True)
	image = models.ImageField(upload_to = upload_location, null = True, blank = True, height_field = 'height_field', width_field = 'width_field')
	height_field = models.IntegerField(default = 0)
	width_field = models.IntegerField(default = 0)
	content = models.TextField() #max_lenght = more than CharField
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	# for Python 2
	#def __unicode__(self):
	#	return self.title

	#for Python3
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("detail", kwargs={"id": self.id})
		#return "/posts/%s/" %(self.id)
	class Meta:
		ordering = ['-timestamp', '-updated']



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class VEHICLE(models.Model):
	Vehicle_no=models.CharField(max_length=15)
	Driver_name=models.CharField(max_length=25)
	Mob_no=models.CharField(max_length=12)
	Status=models.CharField(max_length=15)
	City=models.CharField(max_length=20)
	Latitude=models.CharField(max_length=15)
	Longitude=models.CharField(max_length=15)




	def __str__(self):
		return self.Vehicle_no+","+self.Mob_no+","+self.Status+","+self.Driver_name+","+self.City
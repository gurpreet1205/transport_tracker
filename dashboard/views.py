# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import requests
import json
import sqlite3
from dashboard.models import VEHICLE
import random
def maps(request):
	city=[]
	status=[]
	v_no=[]
	name=[]
	mob_no=[]
	z=[]
	details=VEHICLE.objects.all()
	for x in details:
		x=str(x)
		l=x.split(',')
		v_no.append(l[0])
		mob_no.append(l[1])
		status.append(l[2])
		name.append(l[3])
		city.append(l[4])
		z.append(int(random.random()*10000)%60)
	detail=zip(name,mob_no,v_no,status,z)
	print z
	return render( request , "home.html",{ "detail" : detail })

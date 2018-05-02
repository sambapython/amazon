# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VM(models.Model):
	name=models.CharField(max_length=250)
	harddisk=models.IntegerField()
	ram=models.IntegerField()
	cpu_cores=models.IntegerField()
	instance=models.CharField(max_length=250)
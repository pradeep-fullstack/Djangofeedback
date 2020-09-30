from django.db import models

class Regfact(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	pas=models.CharField(max_length=200)
	num=models.CharField(max_length=200)
	def __str__(self):
		return self.name+" "+self.email+" "+self.pas+" "+self.num

	
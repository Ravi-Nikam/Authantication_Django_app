from django.db import models

# Create your models here.
class Emp_reg(models.Model):
	name = models.CharField(max_length=10)
	email = models.CharField(max_length=25,primary_key=True)
	mobileno = models.IntegerField()
	password = models.CharField(max_length=25)


	def __str__(self):
		return self.email
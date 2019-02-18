from django.db import models

# Create your models here.
class Survey(models.Model):
	name = models.CharField(max_length=30)
	phone = models.IntegerField()
	gender = models.CharField(max_length=4)
	home = models.CharField(max_length=100)
	work = models.CharField(max_length=100)

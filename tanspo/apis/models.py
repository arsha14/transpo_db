from django.db import models

# Create your models here.
class Questionaire(models.Model):
	question = models.CharField(max_length= 1400)

class Interviewer(models.Model):
	username = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	questions = models.ManyToManyField(Questionaire, blank=True)

	def __str__(self):
		return self.username
	

class Survey(models.Model):
	interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=True)
	phone = models.IntegerField()
	gender = models.CharField(max_length=4, blank=True)
	home = models.CharField(max_length=100, blank=True)
	work = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name

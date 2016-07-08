from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=250)
	question_descripton = models.CharField(max_length=400, default="")
	pub_date = models.DateTimeField('date published')
	voted_users = models.ManyToManyField(User, blank=True,)
	total_votes = models.IntegerField(default=0)
	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	percentage = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text


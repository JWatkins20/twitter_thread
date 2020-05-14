from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class Message(models.Model):
	text = models.TextField(max_length=280)

class Thread(models.Model):
	text = models.TextField(max_length=255)
	messages = models.ManyToManyField(Message, blank=True)

class User(AbstractUser):
	threads = models.ManyToManyField(Thread, blank=True)
	request_token = models.CharField(blank=True, max_length=255)
	request_token_secret = models.CharField(blank=True, max_length=255)
	access_token = models.CharField(blank=True, max_length=255)
	access_token_secret = models.CharField(blank=True, max_length=255)
	post_permissions = models.BooleanField(default=False)
	class Meta:
		app_label = "user"
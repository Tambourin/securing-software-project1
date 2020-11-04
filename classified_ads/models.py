from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ad(models.Model):
  creator = models.TextField()
  text = models.TextField()

class PoorUser(models.Model):
  username = models.TextField()
  password = models.TextField()
from django.db import models

# Create your models here.
class SimpleUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
# Create your models here.

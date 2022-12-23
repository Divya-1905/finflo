from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
class nonworker(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
class pagenotes(models.Model):
    note = models.CharField(max_length=200)
    content = models.CharField(max_length=300)
        

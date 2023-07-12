from django.db import models

# Create your models here.

class Test(models.Model):
    numb = models.IntegerField(default=0)
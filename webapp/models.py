from django.db import models

class CalcModel(models.Model):
    out = models.DateTimeField()
    to = models.DateTimeField()

# Create your models here.

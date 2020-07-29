import os
from django.conf import settings
from django.db import models

class Certificates(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=20)
    #image=models.FilePathField(path="my_certificates/static/img", recursive= True, blank = True)
    image = models.CharField(max_length=100)
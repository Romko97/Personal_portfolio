from django.db import models

class Certificates(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=20)
    image=models.ImageField(default='default.jpg', upload_to='static/img')
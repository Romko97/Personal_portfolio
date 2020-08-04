from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.ManyToManyField("Technology", related_name="Project")
    GitHub=models.CharField(max_length=255, default='Sorry, i will add GitHub link as soon as possible')
   # image=models.FilePathField(path="/projects/static/img", recursive= True)
    image=models.CharField(max_length=100)


class Technology(models.Model):
    name = models.ManyToManyField("Project", related_name="Technology")
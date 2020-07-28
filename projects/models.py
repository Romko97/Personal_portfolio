from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=20)
    image=models.ImageField(default='default.jpg', upload_to='static/img', blank=True,)
    def get_pic(self):
        if self.pic:
            return self.pic
        return ImageFieldFile(instance=None, field=FileField(),
                              name='static/img/default.jpg')

class Technology(models.Model):
    name = models.CharField(max_length=100)
from django.db import models
# used dynamic backend
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/', verbose_name='Image')


def __str__(self):
    return self.title
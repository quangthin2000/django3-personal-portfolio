from operator import mod
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='project/images')
    url = models.CharField(max_length=127)
    created_at = models.DateField()
    def __str__(self):
        return self.title
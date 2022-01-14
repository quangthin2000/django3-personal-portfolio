from django.db import models
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    tag = models.CharField(max_length=32)
    created_at = models.DateField()
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class PhotoComment(models.Model):
  rating = models.IntegerField()
  comment = models.TextField()
  date = models.DateField()
  url = models.URLField()

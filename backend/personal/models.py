from django.db import models

class Project(models.Model):
  date_created = models.DateTimeField()
  last_update = models.DateTimeField()
  name = models.CharField(max_length=100)
  link = models.URLField()
  picture = models.ImageField()
  


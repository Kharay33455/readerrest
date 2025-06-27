from django.db import models

# Create your models here.

class Statement(models.Model):
    file = models.FileField(upload_to="statement/")

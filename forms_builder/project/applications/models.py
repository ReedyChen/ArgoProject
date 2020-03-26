from django.db import models

# Create your models here.

class Application(models.Model):

    # already applied for this semester
    applied = models.BooleanField(default = False)
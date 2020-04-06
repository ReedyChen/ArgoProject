from django.db import models
from forms.models import *
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Application(models.Model):

    applied = models.BooleanField(default = False) 
    subject = models.CharField(max_length=4)
    application_name = models.CharField(max_length=50, default = 'none')

    conudctor = models.CharField(max_length=50, default = 'none')
    time_slots = models.CharField(max_length=500, default = '[]')

class ProgramGroup(models.Model):
    name = models.CharField(max_length = 50)
    intro = models.TextField(help_text="Enter the introduction of this group of program", blank=True)
    the_form = models.OneToOneField(Form, null = True, on_delete = models.PROTECT, help_text="The form that is used to help matching")
    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length = 50)
    intro = models.TextField(help_text="Enter the introduction of this program", blank=True)
    group = models.ForeignKey(ProgramGroup, on_delete = models.CASCADE, help_text="The group which this program belong")
    size = models.IntegerField(validators=[MinValueValidator(0)], default = 10, help_text="How many people expected in this program")
    def __str__(self):
        return self.name + "(" + self.group.name + ")"
    def save(self, *args, **kwargs):
        
        super(Program, self).save(*args, **kwargs)


class Feature(models.Model):
    name = models.OneToOneField(Field, on_delete = models.CASCADE)
    weight = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=1)
    program = models.ForeignKey(Program, on_delete = models.CASCADE)
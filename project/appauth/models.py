from __future__ import unicode_literals

import datetime
import django

from forms.models import *
from django import forms
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete = models.CASCADE,)
    time_creation = models.DateTimeField()
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    

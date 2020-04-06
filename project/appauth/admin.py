from __future__ import unicode_literals

import datetime
import django

from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ['user']

admin.site.register(UserProfile, UserProfileAdmin)
#admin.site.register(Form, FormAdmin)

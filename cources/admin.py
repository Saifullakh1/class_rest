from django.contrib import admin

from cources.models import *

admin.site.register(Course)
admin.site.register(Exercise)
admin.site.register(Exercise_file)
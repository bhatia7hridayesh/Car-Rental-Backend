from django.contrib import admin
from .models import *
from django_q import models as q_models
from django_q import admin as q_admin

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Vehicle_Bookings_Log)


admin.site.unregister([q_models.Failure])
@admin.register(q_models.Failure)
class ChildClassAdmin(q_admin.FailAdmin):
    list_display = (
        'name',
        'func',
        'result',
        'started',
        # add attempt_count to list_display
        'attempt_count'
    )
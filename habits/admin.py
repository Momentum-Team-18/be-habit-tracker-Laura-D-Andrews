from django.contrib import admin
from .models import User, Tracker, Record

admin.site.register(User)
admin.site.register(Tracker)
admin.site.register(Record)

# Register your models here.

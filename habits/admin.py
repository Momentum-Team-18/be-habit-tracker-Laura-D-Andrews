from django.contrib import admin
from .models import User, Tracker, Record, Profile

admin.site.register(User)
admin.site.register(Tracker)
admin.site.register(Record)
admin.site.register(Profile)

# Register your models here.

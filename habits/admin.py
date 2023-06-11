from django.contrib import admin
from .models import User, Tracker, Record, Profile, Follower

admin.site.register(User)
admin.site.register(Tracker)
admin.site.register(Record)
admin.site.register(Profile)
admin.site.register(Follower)

# Register your models here.

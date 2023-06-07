
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
    HEALTHCARE = 'HC'
    EDUCATION = 'ED'
    TECH_INDUSTRY = 'TECH'
    LAW = 'LAW'
    RETAIL = 'RETAIL'
    CUSTOMER_SERVICE = 'CS'
    SERVICE_INDUSTRY = 'SI'
    SELF_EMPLOYED = 'SE'
    UNEMPLOYED = 'UNEMP'
    PARENT_OR_GUARDIAN = 'POG'
    STUDENT = 'ST'
    OTHER = 'OT'

    OCCUPATION_CHOICES = [
        (HEALTHCARE, 'healthcare'),
        (EDUCATION, 'education'),
        (TECH_INDUSTRY, 'tech industry'),
        (LAW, 'law'),
        (RETAIL, 'retail'),
        (CUSTOMER_SERVICE, 'customer service'),
        (SERVICE_INDUSTRY, 'service industry'),
        (SELF_EMPLOYED, 'self employed'),
        (UNEMPLOYED, 'unemployed'),
        (PARENT_OR_GUARDIAN, 'parent or guardian'),
        (STUDENT, 'student'),
        (OTHER, 'other'),

    ]
    birthdate = models.DateField(blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=30, choices=OCCUPATION_CHOICES)


class Tracker(models.Model):

    GOAL_MET_CHOICES = [(False, 'No'), (True, 'yes')]
    goal = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    goal_met = models.BooleanField(default=False, choices=GOAL_MET_CHOICES)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='user_trackers')

    def __str__(self):
        return self.goal

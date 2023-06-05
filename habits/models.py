from django.db import models
from django.contrib.auth.models import AbstractUser
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

    OCCUPATION_CHOICES = [
        (HEALTHCARE, 'healthcare'),
        (EDUCATION, 'education'),
        (TECH_INDUSTRY, 'tech industry'),
        (LAW, 'law'),
        (RETAIL, 'retail'),
        (CUSTOMER_SERVICE, 'customer service'),
        (SERVICE_INDUSTRY, 'service industry'),
        (SELF_EMPLOYED, 'self employed'),
        (UNEMPLOYED, 'unembloyed'),
        (PARENT_OR_GUARDIAN, 'parent or guardian'),
        (STUDENT, 'student'),

    ]
    birthdate = models.DateField(blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=30, choices=OCCUPATION_CHOICES)


class Tracker(models.Model):
    FITNESS = 'FIT'
    SLEEP = 'SL'
    HEALTH_WELLNESS = 'HW'
    QUIT_BAD_HABIT = 'QBH'
    HOUSEHOLD = 'HH'

    CATEGORY_CHOICES = [
        (FITNESS, 'Fitness'),
        (SLEEP, 'Sleep'),
        (HEALTH_WELLNESS, 'Health and Wellness'),
        (QUIT_BAD_HABIT, 'Quit a Bad Habit'),
        (HOUSEHOLD, 'household'),

    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    number_days_week = models.IntegerField()
    times_a_day = models.IntegerField(blank=True, null=True)
    length_in_minutes = models.FloatField(default=0, blank=True, null=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='user_trackers')

    def __str__(self):
        return self.name

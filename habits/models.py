
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.query import QuerySet
from django.utils import timezone
import django_filters
# Create your models here.


class User(AbstractUser):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='user_constraint')]


class Profile(models.Model):
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
    postcode = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=30, choices=OCCUPATION_CHOICES)
    birthdate = models.DateField(blank=True, null=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="user_profile",
        blank=True, null=True)


class Tracker(models.Model):
    goal = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='user_trackers')

    def __str__(self):
        return self.goal


class RecordManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-date')


class Record(models.Model):
    GOAL_MET_CHOICES = [(False, 'No'), (True, 'Yes')]
    record_number = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    objects = RecordManager()
    goal_met = models.BooleanField(default=True, choices=GOAL_MET_CHOICES)
    tracker = models.ForeignKey(
        to=Tracker, on_delete=models.CASCADE, related_name='tracker_record',
        default=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'tracker'], name='tracker_constraint')
        ]

    def __str__(self):
        return self.tracker

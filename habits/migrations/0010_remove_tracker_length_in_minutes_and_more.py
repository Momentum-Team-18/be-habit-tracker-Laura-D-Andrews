# Generated by Django 4.2.2 on 2023-06-07 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0009_alter_user_occupation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='length_in_minutes',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='number_days_week',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='times_a_day',
        ),
        migrations.AddField(
            model_name='tracker',
            name='date',
            field=models.DateField(default='1988-02-07'),
        ),
        migrations.AddField(
            model_name='tracker',
            name='target',
            field=models.IntegerField(default=0),
        ),
    ]
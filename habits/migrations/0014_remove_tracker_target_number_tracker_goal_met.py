# Generated by Django 4.2.2 on 2023-06-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0013_remove_tracker_action_alter_tracker_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='target_number',
        ),
        migrations.AddField(
            model_name='tracker',
            name='goal_met',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'yes')], default=False, verbose_name='Goal Met?'),
        ),
    ]
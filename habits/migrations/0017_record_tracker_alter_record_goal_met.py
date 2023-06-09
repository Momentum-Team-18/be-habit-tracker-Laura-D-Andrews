# Generated by Django 4.2.2 on 2023-06-07 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0016_record_remove_tracker_date_remove_tracker_goal_met'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='tracker',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='tracker_record', to='habits.tracker'),
        ),
        migrations.AlterField(
            model_name='record',
            name='goal_met',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False),
        ),
    ]

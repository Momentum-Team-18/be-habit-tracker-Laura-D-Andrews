# Generated by Django 4.2.2 on 2023-06-07 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0011_rename_target_tracker_target_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='target_action',
            new_name='action',
        ),
        migrations.RenameField(
            model_name='tracker',
            old_name='name',
            new_name='goal',
        ),
        migrations.AlterField(
            model_name='tracker',
            name='date',
            field=models.DateField(default='2023-02-07'),
        ),
    ]
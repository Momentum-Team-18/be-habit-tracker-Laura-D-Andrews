# Generated by Django 4.2.2 on 2023-06-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_alter_tracker_length_in_minutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='date',
            field=models.DateField(default='1988-02-07'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-11 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0033_remove_user_profile_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='goal_met',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=True),
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

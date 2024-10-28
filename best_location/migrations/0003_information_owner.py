# Generated by Django 4.1.5 on 2023-10-30 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('best_location', '0002_remove_information_holding_the_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='owner',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.1.5 on 2023-10-30 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best_location', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='holding_the_event',
        ),
    ]

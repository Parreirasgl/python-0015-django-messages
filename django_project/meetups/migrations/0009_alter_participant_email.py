# Generated by Django 5.0.3 on 2024-04-11 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0008_participant_address_participant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

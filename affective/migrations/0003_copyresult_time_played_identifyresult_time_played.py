# Generated by Django 4.1.5 on 2023-01-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affective', '0002_copyresult_identifyresult_delete_result_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='copyresult',
            name='time_played',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='identifyresult',
            name='time_played',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
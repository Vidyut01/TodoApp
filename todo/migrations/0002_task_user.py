# Generated by Django 4.1 on 2023-06-14 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="user",
            field=models.CharField(max_length=100, null=True),
        ),
    ]

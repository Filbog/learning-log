# Generated by Django 5.0.6 on 2024-05-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0003_topic_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="public",
            field=models.BooleanField(default=False),
        ),
    ]

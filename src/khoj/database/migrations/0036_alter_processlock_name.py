# Generated by Django 4.2.10 on 2024-04-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0035_processlock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="processlock",
            name="name",
            field=models.CharField(
                choices=[("index_content", "Index Content"), ("scheduled_job", "Scheduled Job")], max_length=200
            ),
        ),
    ]

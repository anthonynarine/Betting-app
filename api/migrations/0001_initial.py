# Generated by Django 4.1.5 on 2023-01-10 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=250)),
            ],
            options={
                "unique_together": {("name", "location")},
            },
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("username", models.CharField(max_length=255)),
                ("title", models.TextField()),
                ("content", models.TextField()),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

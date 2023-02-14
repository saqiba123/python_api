# Generated by Django 4.1.6 on 2023-02-08 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="hotels",
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
                ("Property", models.CharField(max_length=40)),
                ("Rating", models.CharField(max_length=40)),
                ("Destination", models.CharField(max_length=40)),
                ("Country", models.CharField(max_length=40)),
            ],
        ),
    ]

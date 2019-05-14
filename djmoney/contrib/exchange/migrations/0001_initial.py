# Generated by Django 2.0.4 on 2018-04-03 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExchangeBackend",
            fields=[
                ("name", models.CharField(max_length=255, primary_key=True, serialize=False)),
                ("last_update", models.DateTimeField(auto_now=True)),
                ("base_currency", models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name="Rate",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("currency", models.CharField(max_length=3)),
                ("value", models.DecimalField(decimal_places=6, max_digits=20)),
                (
                    "backend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exchange.ExchangeBackend", related_name="rates"
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(name="rate", unique_together={("currency", "backend")}),
    ]

# Generated by Django 5.0.6 on 2024-06-11 21:12

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TreatmentRecords",
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
                (
                    "date_of_diagnosis",
                    models.DateField(default=django.utils.timezone.now),
                ),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="animal.animal"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicineTreatment",
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
                ("name_of_vet", models.CharField(max_length=50)),
                (
                    "date_of_medicine_treatment",
                    models.DateField(default=django.utils.timezone.now),
                ),
                (
                    "current_state",
                    models.CharField(
                        choices=[("D", "dead"), ("C", "cured")], max_length=1
                    ),
                ),
                (
                    "cured",
                    models.CharField(
                        choices=[("S", "sold"), ("N", "not sold")], max_length=1
                    ),
                ),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="animal.treatmentrecords",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Dosagetreatment",
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
                ("name_of_vet", models.CharField(max_length=50)),
                (
                    "date_of_medicine_treatment",
                    models.DateField(default=django.utils.timezone.now),
                ),
                ("dosage_treatment_used", models.CharField(max_length=50)),
                (
                    "current_state",
                    models.CharField(
                        choices=[("D", "dead"), ("C", "cured")], max_length=1
                    ),
                ),
                (
                    "cured",
                    models.CharField(
                        choices=[("S", "sold"), ("N", "not sold")], max_length=1
                    ),
                ),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="animal.treatmentrecords",
                    ),
                ),
            ],
        ),
    ]

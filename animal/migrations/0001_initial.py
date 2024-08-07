# Generated by Django 5.0.6 on 2024-07-18 08:30

import datetime
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnimalBase",
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
                    "animal_name",
                    models.CharField(
                        max_length=50,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="static/default.jpg", upload_to="animals/%Y/%m/%d/"
                    ),
                ),
                (
                    "breed",
                    models.CharField(
                        max_length=50,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "male"), ("F", "female")], max_length=1
                    ),
                ),
                (
                    "date_of_next_service",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        help_text="Only applicable for female",
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AInonPredeterminedServicedAnimal",
            fields=[
                (
                    "animalbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="animal.animalbase",
                    ),
                ),
                (
                    "date_of_service",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 7, 18, 8, 30, 52, 513562, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 7, 18, 8, 30, 52, 513581, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
            ],
            options={
                "verbose_name": "ai_non_predetermined",
            },
            bases=("animal.animalbase",),
        ),
        migrations.CreateModel(
            name="AIPredeterminedServiceAnimal",
            fields=[
                (
                    "animalbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="animal.animalbase",
                    ),
                ),
                (
                    "date_of_service",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 7, 18, 8, 30, 52, 513201, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 7, 18, 8, 30, 52, 513221, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
            ],
            options={
                "verbose_name": "ai_predetermined",
            },
            bases=("animal.animalbase",),
        ),
        migrations.CreateModel(
            name="LocallyServicedAnimal",
            fields=[
                (
                    "animalbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="animal.animalbase",
                    ),
                ),
                (
                    "name_of_owner",
                    models.CharField(
                        max_length=50,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "date_of_service",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 7, 18, 8, 30, 52, 512826, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 7, 18, 8, 30, 52, 512843, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
            ],
            options={
                "verbose_name": "locally_serviced",
            },
            bases=("animal.animalbase",),
        ),
        migrations.CreateModel(
            name="PurchasedAnimal",
            fields=[
                (
                    "animalbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="animal.animalbase",
                    ),
                ),
                (
                    "seller_name",
                    models.CharField(
                        max_length=50,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "date_purchased",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 7, 18, 8, 30, 52, 512430, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
            ],
            options={
                "verbose_name": "purchased",
            },
            bases=("animal.animalbase",),
        ),
        migrations.CreateModel(
            name="DosageTreatment",
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
                ("date_of_diagnosis", models.DateField(auto_now_add=True)),
                (
                    "name_of_vet",
                    models.CharField(
                        max_length=50,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                ("date_of_medication", models.DateField(auto_now_add=True)),
                (
                    "current_state",
                    models.CharField(
                        choices=[("cured", "Cured"), ("dead", "Dead")], max_length=50
                    ),
                ),
                (
                    "sold_status",
                    models.CharField(
                        blank=True,
                        choices=[("sold", "Sold"), ("not_sold", "Not Sold")],
                        help_text="Select only if animal is cured.",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "animal_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="animal.animalbase",
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
                ("date_of_diagnosis", models.DateField(auto_now_add=True)),
                (
                    "name_of_vet",
                    models.CharField(
                        max_length=50,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                ("date_of_medication", models.DateField(auto_now_add=True)),
                (
                    "current_state",
                    models.CharField(
                        choices=[("cured", "Cured"), ("dead", "Dead")], max_length=50
                    ),
                ),
                (
                    "sold_status",
                    models.CharField(
                        blank=True,
                        choices=[("sold", "Sold"), ("not_sold", "Not Sold")],
                        help_text="Select only if animal is cured.",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "animal_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="animal.animalbase",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-03 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal", "0002_alter_disposal_date_of_disposal_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="animalbase",
            name="weight",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="disposal",
            name="date_of_disposal",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 3, 18, 16, 34, 200328, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="dosagetreatment",
            name="date_of_diagnosis",
            field=models.DateField(default=datetime.date(2024, 9, 3)),
        ),
        migrations.AlterField(
            model_name="locallyservicedanimal",
            name="birth_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 3, 18, 16, 34, 199154, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="locallyservicedanimal",
            name="expected_maturity_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 3, 18, 16, 34, 199169, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="medicinetreatment",
            name="date_of_diagnosis",
            field=models.DateField(default=datetime.date(2024, 9, 3)),
        ),
        migrations.AlterField(
            model_name="medicinetreatment",
            name="date_of_medication",
            field=models.DateField(default=datetime.date(2024, 9, 3)),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="date_of_birth",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 3, 18, 16, 34, 198810, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="date_purchased",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 3, 18, 16, 34, 198867, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="expected_maturity_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 3, 18, 16, 34, 198831, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]

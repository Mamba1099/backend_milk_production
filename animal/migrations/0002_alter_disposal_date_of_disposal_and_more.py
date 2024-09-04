# Generated by Django 5.0.6 on 2024-08-30 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disposal",
            name="date_of_disposal",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 8, 30, 21, 20, 38, 338062, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="locallyservicedanimal",
            name="birth_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 8, 30, 21, 20, 38, 336752, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="locallyservicedanimal",
            name="expected_maturity_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 8, 30, 21, 20, 38, 336773, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="date_of_birth",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 8, 30, 21, 20, 38, 336335, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="date_purchased",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 8, 30, 21, 20, 38, 336417, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="expected_maturity_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 8, 30, 21, 20, 38, 336366, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]

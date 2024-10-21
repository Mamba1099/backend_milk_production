# Generated by Django 5.0.6 on 2024-09-25 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal", "0005_alter_disposal_date_of_disposal_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disposal",
            name="date_of_disposal",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 25, 18, 54, 43, 192764, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="dosagetreatment",
            name="date_of_diagnosis",
            field=models.DateField(default=datetime.date(2024, 9, 25)),
        ),
        migrations.AlterField(
            model_name="locallyservicedanimal",
            name="birth_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 25, 18, 54, 43, 191491, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="locallyservicedanimal",
            name="expected_maturity_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 25, 18, 54, 43, 191507, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="medicinetreatment",
            name="date_of_diagnosis",
            field=models.DateField(default=datetime.date(2024, 9, 25)),
        ),
        migrations.AlterField(
            model_name="medicinetreatment",
            name="date_of_medication",
            field=models.DateField(default=datetime.date(2024, 9, 25)),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="date_of_birth",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 25, 18, 54, 43, 191130, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="date_purchased",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 25, 18, 54, 43, 191189, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="expected_maturity_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 25, 18, 54, 43, 191151, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="servingbase",
            name="date_presented",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 25, 18, 54, 43, 193140, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="servingbase",
            name="expected_date_of_delivery",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(
                    2024, 9, 25, 18, 54, 43, 193192, tzinfo=datetime.timezone.utc
                ),
                help_text="Only applicable if status is confirmed.",
                null=True,
            ),
        ),
    ]

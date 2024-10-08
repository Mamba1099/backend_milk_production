# Generated by Django 5.0.6 on 2024-09-24 23:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animal", "0003_alter_disposal_date_of_disposal_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disposal",
            name="date_of_disposal",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 24, 23, 57, 30, 772056, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="locallyservicedanimal",
            name="birth_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 24, 23, 57, 30, 770858, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="locallyservicedanimal",
            name="expected_maturity_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 24, 23, 57, 30, 770873, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="date_of_birth",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 24, 23, 57, 30, 770506, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="date_purchased",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 24, 23, 57, 30, 770563, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="purchasedanimal",
            name="expected_maturity_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 24, 23, 57, 30, 770526, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="servingbase",
            name="date_presented",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 24, 23, 57, 30, 772333, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="servingbase",
            name="expected_date_of_delivery",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(
                    2024, 9, 24, 23, 57, 30, 772363, tzinfo=datetime.timezone.utc
                ),
                help_text="Only applicable if status is confirmed.",
                null=True,
            ),
        ),
    ]

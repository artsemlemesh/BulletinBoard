# Generated by Django 4.2.3 on 2023-11-26 03:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bboard", "0020_alter_disposablecode_expires_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disposablecode",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 26, 3, 59, 12, 424743, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]

# Generated by Django 4.2.3 on 2023-11-27 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bboard", "0024_alter_disposablecode_expires_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 27, 8, 0, 15, 832278)
            ),
        ),
        migrations.AlterField(
            model_name="disposablecode",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 27, 8, 1, 15, 832676, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]

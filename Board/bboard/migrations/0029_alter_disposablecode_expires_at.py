# Generated by Django 4.2.3 on 2023-11-28 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bboard", "0028_alter_comment_date_alter_disposablecode_expires_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disposablecode",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 28, 0, 33, 56, 883428, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]

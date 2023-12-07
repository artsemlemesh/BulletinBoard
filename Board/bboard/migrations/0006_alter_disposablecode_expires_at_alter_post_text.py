# Generated by Django 4.2.3 on 2023-12-04 03:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bboard", "0005_alter_disposablecode_expires_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disposablecode",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 4, 3, 4, 59, 93173, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.CharField(max_length=255),
        ),
    ]
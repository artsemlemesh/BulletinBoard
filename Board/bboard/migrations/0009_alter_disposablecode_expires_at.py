# Generated by Django 4.2.3 on 2023-12-11 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bboard", "0008_remove_post_image_alter_disposablecode_expires_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disposablecode",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 11, 6, 16, 7, 815328, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-24 17:56

import django.core.validators
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1028_remove_paperlesstask_task_args_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="archive_serial_number",
            field=models.PositiveIntegerField(
                blank=True,
                db_index=True,
                help_text="The position of this document in your physical document archive.",
                null=True,
                unique=False,
                validators=[
                    django.core.validators.MaxValueValidator(4294967295),
                    django.core.validators.MinValueValidator(0),
                ],
                verbose_name="archive serial number",
            ),
        ),
    ]

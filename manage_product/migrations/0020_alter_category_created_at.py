# Generated by Django 4.2.13 on 2024-05-18 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_product', '0019_alter_category_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 18, 22, 15, 16, 273609)),
        ),
    ]

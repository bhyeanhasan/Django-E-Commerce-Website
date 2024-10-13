# Generated by Django 5.0.4 on 2024-04-26 18:52

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_order', '0013_order_address_order_payment_status_and_more'),
        ('manage_product', '0017_alter_category_created_at'),
        ('manage_user', '0017_alter_customer_registered_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='placed_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 11, 52, 34, 98065)),
        ),
        migrations.AlterField(
            model_name='ordereditem',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_user.customer'),
        ),
        migrations.AlterField(
            model_name='ordereditem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_product.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 11, 52, 34, 98065)),
        ),
    ]
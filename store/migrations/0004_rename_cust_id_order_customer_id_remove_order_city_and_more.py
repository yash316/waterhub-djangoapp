# Generated by Django 4.0.2 on 2022-02-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_order_paid_remove_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cust_id',
            new_name='customer_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pincode',
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.2.6 on 2022-03-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]

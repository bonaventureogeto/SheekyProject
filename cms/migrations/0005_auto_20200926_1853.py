# Generated by Django 3.1.1 on 2020-09-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20200926_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='appointment_date',
            field=models.CharField(max_length=255),
        ),
    ]

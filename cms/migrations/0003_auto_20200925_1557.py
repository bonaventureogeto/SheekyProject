# Generated by Django 3.1.1 on 2020-09-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20200925_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='appointment_date',
            field=models.DateField(),
        ),
    ]

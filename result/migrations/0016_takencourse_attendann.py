# pylint: disable-all
# Generated by Django 3.2.23 on 2024-03-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0015_auto_20240308_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='takencourse',
            name='attendann',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-04 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_fboard_b_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 4, 22, 52, 52, 365855)),
        ),
    ]
# Generated by Django 4.2.4 on 2024-04-17 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investimento', models.TextField(max_length=255)),
                ('pago', models.BooleanField(default=False)),
                ('data', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]

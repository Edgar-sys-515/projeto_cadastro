# Generated by Django 4.2.4 on 2024-04-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investimento',
            name='valor',
            field=models.FloatField(null=True),
        ),
    ]
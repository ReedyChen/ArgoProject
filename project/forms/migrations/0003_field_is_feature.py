# Generated by Django 2.2 on 2020-04-06 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20200405_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='is_feature',
            field=models.BooleanField(default=False),
        ),
    ]

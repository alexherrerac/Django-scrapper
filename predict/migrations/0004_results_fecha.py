# Generated by Django 3.2.4 on 2021-09-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_auto_20210924_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

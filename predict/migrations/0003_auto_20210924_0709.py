# Generated by Django 3.2.4 on 2021-09-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_auto_20210919_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='ciudad',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='results',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='results',
            name='profesion',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='results',
            name='universidad',
            field=models.CharField(max_length=30),
        ),
    ]

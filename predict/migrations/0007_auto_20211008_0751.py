# Generated by Django 3.2.4 on 2021-10-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0006_auto_20211002_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='predicciones',
            options={'get_latest_by': 'fecha', 'verbose_name_plural': 'Predicciones'},
        ),
        migrations.AlterField(
            model_name='predicciones',
            name='profesion',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='predicciones',
            name='universidad',
            field=models.CharField(max_length=50),
        ),
    ]

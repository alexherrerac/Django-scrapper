# Generated by Django 3.2.4 on 2021-09-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Busqueda_nombres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('universidad', models.CharField(max_length=30)),
                ('profesion', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('cliente', models.CharField(max_length=30)),
            ],
        ),
    ]

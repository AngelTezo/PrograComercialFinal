# Generated by Django 2.1.3 on 2018-11-22 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]

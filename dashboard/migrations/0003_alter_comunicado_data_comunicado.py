# Generated by Django 4.0.3 on 2022-04-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_comunicados_comunicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='data_comunicado',
            field=models.DateField(),
        ),
    ]

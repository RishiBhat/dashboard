# Generated by Django 3.0 on 2021-11-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211101_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prqty',
            field=models.IntegerField(default=10),
        ),
    ]

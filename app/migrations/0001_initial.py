# Generated by Django 2.2.10 on 2021-10-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField(default=20)),
                ('address', models.TextField(max_length=10000)),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('maritialstatus', models.CharField(choices=[('Married', 'married'), ('Engaged', 'engaged'), ('Unmarried', 'unmarried')], max_length=50)),
                ('urimage', models.ImageField(blank=True, default='', upload_to='image/')),
                ('urdoc', models.FileField(blank=True, upload_to='files/')),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]

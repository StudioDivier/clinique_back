# Generated by Django 3.1.2 on 2020-11-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique_app', '0006_auto_20201113_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.CharField(max_length=128)),
                ('service', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='GetPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

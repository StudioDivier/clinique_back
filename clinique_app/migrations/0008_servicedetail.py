# Generated by Django 3.1.2 on 2020-11-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique_app', '0007_appointment_getprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('img', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=1024)),
                ('time_operation', models.CharField(max_length=128)),
                ('sex', models.CharField(max_length=64)),
                ('reabilitation', models.CharField(max_length=128)),
                ('time_result', models.CharField(max_length=128)),
                ('amnesia', models.CharField(max_length=128)),
                ('part_name', models.CharField(max_length=128)),
                ('session_price1', models.DecimalField(decimal_places=2, max_digits=9)),
                ('session_price2', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]

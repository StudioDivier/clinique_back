# Generated by Django 3.1.2 on 2020-11-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique_app', '0022_popular'),
    ]

    operations = [
        migrations.CreateModel(
            name='qa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=128)),
                ('answer', models.TextField(max_length=2048)),
            ],
        ),
    ]

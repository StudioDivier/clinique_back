# Generated by Django 3.1.2 on 2020-11-17 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique_app', '0016_servicedetail_short_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='personals',
            name='photo_index_slider',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]

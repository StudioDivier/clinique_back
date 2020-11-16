# Generated by Django 3.1.2 on 2020-11-16 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinique_app', '0009_auto_20201116_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinique_app.serviceslist'),
            preserve_default=False,
        ),
    ]

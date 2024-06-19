# Generated by Django 5.0.6 on 2024-06-19 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='location_id'),
        ),
        migrations.CreateModel(
            name='spectacle',
            fields=[
                ('spectacle_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=60, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255, null=True)),
                ('poster_url', models.CharField(max_length=255, null=True)),
                ('duration', models.SmallIntegerField(null=True)),
                ('created_in', models.CharField(max_length=4, null=True)),
                ('bookable', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spectacles', to='catalogue.location')),
            ],
            options={
                'db_table': 'spectacles',
            },
        ),
    ]

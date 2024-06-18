# Generated by Django 5.0.6 on 2024-06-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('locality_id', models.AutoField(primary_key=True, serialize=False)),
                ('postal_code', models.CharField(max_length=6)),
                ('locality', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'localities',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='artist_id'),
        ),
    ]

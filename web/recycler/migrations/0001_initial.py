# Generated by Django 5.0.6 on 2024-05-20 11:14

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recycler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('PhoneNumber', models.CharField(max_length=255)),
                ('Location', django.contrib.gis.db.models.fields.PointField(default='POINT(0 0)', srid=4326)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

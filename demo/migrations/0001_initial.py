# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_contact', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('number_of_bedrooms', models.PositiveIntegerField()),
                ('property_name', models.CharField(max_length=50)),
                ('max_occupants', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('lease_term', models.PositiveIntegerField()),
                ('maximum_income', models.PositiveIntegerField()),
                ('minimum_income', models.PositiveIntegerField()),
                ('income_divisor', models.PositiveIntegerField()),
                ('bus_transit', models.CharField(max_length=20)),
                ('rail_transit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('default_contact', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentOwner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('default_contact', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='managed_by',
            field=models.ForeignKey(to='demo.ApartmentManager'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='owned_by',
            field=models.ForeignKey(to='demo.ApartmentOwner'),
        ),
    ]

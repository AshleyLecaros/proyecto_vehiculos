# Generated by Django 4.2.11 on 2024-05-22 19:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('registration_plate', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('year', models.DateField()),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'driver',
                'verbose_name_plural': 'drivers',
                'ordering': ['registration_plate'],
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('vehicle', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='driver', to='vehiculos_app.vehicle')),
            ],
            options={
                'verbose_name': 'driver',
                'verbose_name_plural': 'drivers',
                'ordering': ['rut'],
            },
        ),
        migrations.CreateModel(
            name='AccountingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_purchase', models.DateField()),
                ('price', models.FloatField()),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='accouting', to='vehiculos_app.vehicle')),
            ],
            options={
                'verbose_name': 'Accounting Record',
                'verbose_name_plural': 'Accounting Records',
                'ordering': ['date_of_purchase'],
            },
        ),
    ]

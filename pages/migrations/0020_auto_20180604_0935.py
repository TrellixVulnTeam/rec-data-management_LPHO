# Generated by Django 2.0.5 on 2018-06-04 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20180604_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataInSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Data')),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('facility', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=10)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=6)),
                ('year', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=9)),
                ('week', models.CharField(max_length=10)),
                ('day_of_month', models.CharField(max_length=10)),
                ('day_of_week', models.CharField(max_length=9)),
                ('time', models.CharField(max_length=7)),
                ('units', models.CharField(max_length=10)),
                ('value', models.IntegerField()),
                ('data', models.ManyToManyField(through='pages.DataInSet', to='pages.Data')),
            ],
        ),
        migrations.AddField(
            model_name='datainset',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Dataset'),
        ),
    ]

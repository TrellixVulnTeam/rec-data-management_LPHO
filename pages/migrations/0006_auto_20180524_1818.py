# Generated by Django 2.0.5 on 2018-05-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20180524_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='weekday',
            new_name='day_of_week',
        ),
        migrations.AddField(
            model_name='data',
            name='day_of_month',
            field=models.CharField(default=1, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='month',
            field=models.CharField(default='January', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='year',
            field=models.CharField(default=2000, max_length=4),
            preserve_default=False,
        ),
    ]
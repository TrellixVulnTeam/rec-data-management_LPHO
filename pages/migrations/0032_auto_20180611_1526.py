# Generated by Django 2.0.5 on 2018-06-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_auto_20180611_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartset',
            name='name',
            field=models.CharField(default='name', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chartset',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

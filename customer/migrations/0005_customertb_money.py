# Generated by Django 2.2.5 on 2020-01-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_customertb_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='customertb',
            name='money',
            field=models.IntegerField(default=0, verbose_name='余额'),
        ),
    ]

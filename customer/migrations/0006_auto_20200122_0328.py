# Generated by Django 2.2.5 on 2020-01-22 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customertb_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='customertb',
            name='redirect_url',
            field=models.CharField(default='https://arnotest.com', max_length=64, verbose_name='下载页URL'),
        ),
        migrations.AddField(
            model_name='customertb',
            name='udid_url',
            field=models.CharField(default='https://arnotest.com', max_length=64, verbose_name='IPA回调URL'),
        ),
    ]

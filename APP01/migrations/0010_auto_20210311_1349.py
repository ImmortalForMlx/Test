# Generated by Django 2.1 on 2021-03-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0009_auto_20210311_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='pwd',
            field=models.CharField(max_length=32),
        ),
    ]
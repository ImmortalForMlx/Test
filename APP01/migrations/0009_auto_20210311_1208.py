# Generated by Django 2.1 on 2021-03-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0008_auto_20210311_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='pwd',
            field=models.IntegerField(),
        ),
    ]

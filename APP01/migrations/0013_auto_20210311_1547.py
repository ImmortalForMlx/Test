# Generated by Django 2.1.1 on 2021-03-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0012_remove_userinfo_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pwd',
            field=models.CharField(max_length=32, null=True),
        ),
    ]

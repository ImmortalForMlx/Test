# Generated by Django 2.1 on 2021-03-11 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='country',
            field=models.CharField(max_length=32, null=True),
        ),
    ]

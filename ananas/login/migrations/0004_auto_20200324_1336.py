# Generated by Django 3.0.1 on 2020-03-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200324_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='naissance',
            field=models.CharField(max_length=10),
        ),
    ]

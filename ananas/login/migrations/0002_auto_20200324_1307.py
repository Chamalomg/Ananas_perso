# Generated by Django 3.0.1 on 2020-03-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='promo',
            field=models.IntegerField(),
        ),
    ]
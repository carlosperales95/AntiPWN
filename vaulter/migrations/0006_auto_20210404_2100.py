# Generated by Django 3.1.7 on 2021-04-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaulter', '0005_auto_20210404_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safe',
            name='service',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='safe',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]

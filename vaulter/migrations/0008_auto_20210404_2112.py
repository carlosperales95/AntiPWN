# Generated by Django 3.1.7 on 2021-04-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaulter', '0007_auto_20210404_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safe',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='safe',
            name='service',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='safe',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]

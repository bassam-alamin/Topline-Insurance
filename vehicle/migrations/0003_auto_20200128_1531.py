# Generated by Django 2.2.7 on 2020-01-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20200128_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='phone_no',
            field=models.CharField(max_length=13),
        ),
    ]

# Generated by Django 2.0.1 on 2018-05-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poopdeck', '0008_auto_20180503_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='CalenderDate',
            field=models.DateField(),
        ),
    ]

# Generated by Django 2.0.1 on 2018-05-02 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poopdeck', '0004_auto_20180430_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='Event',
        ),
        migrations.AddField(
            model_name='events',
            name='Day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='poopdeck.Day'),
        ),
    ]

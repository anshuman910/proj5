# Generated by Django 3.0.6 on 2020-06-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20200614_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknumber',
            name='isbn_12',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20200510_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, default=0, max_length=7),
        ),
    ]

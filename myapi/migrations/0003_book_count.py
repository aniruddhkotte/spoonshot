# Generated by Django 3.1.2 on 2020-10-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20201030_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]

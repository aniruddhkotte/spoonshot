# Generated by Django 3.1.2 on 2020-10-30 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_book_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]

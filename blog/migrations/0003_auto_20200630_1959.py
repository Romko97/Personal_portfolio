# Generated by Django 3.0.7 on 2020-06-30 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200630_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoties',
            new_name='categories',
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_certificates', '0004_auto_20200729_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='image_uploud',
            field=models.FilePathField(blank=True, path='my_certificates/static/img', recursive=True),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='image',
            field=models.FilePathField(path='my_certificates/static/img'),
        ),
    ]
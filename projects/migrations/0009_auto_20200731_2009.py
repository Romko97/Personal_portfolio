# Generated by Django 3.0.7 on 2020-07-31 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200731_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.ManyToManyField(related_name='Project', to='projects.Technology'),
        ),
        migrations.RemoveField(
            model_name='technology',
            name='name',
        ),
        migrations.AddField(
            model_name='technology',
            name='name',
            field=models.ManyToManyField(related_name='Technology', to='projects.Project'),
        ),
    ]

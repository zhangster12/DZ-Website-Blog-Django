# Generated by Django 3.2.2 on 2021-05-16 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='excerpt',
        ),
    ]
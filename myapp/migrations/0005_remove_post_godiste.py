# Generated by Django 5.0 on 2024-11-13 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_post_pozicija'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='godiste',
        ),
    ]

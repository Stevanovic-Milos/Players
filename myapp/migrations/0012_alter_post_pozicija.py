# Generated by Django 5.0 on 2024-11-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pozicija',
            field=models.CharField(blank=True, choices=[('Golman', 'Golman'), ('Zadnji vezni', 'Zadnji vezni'), ('Prednji vezni', 'Prednji vezni'), ('Špic', 'Špic'), ('Levo krilo', 'Levo krilo'), ('Desno krilo', 'Desno krilo'), ('Levi bek', 'Levi bek'), ('Desni bek', 'Desni bek'), ('Štoper', 'Štoper')], default='Prednji vezni', max_length=20, null=True),
        ),
    ]

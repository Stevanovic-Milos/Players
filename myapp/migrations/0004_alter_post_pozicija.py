# Generated by Django 5.0 on 2024-11-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_post_pozicija'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pozicija',
            field=models.CharField(blank=True, choices=[('Golman', 'Golman'), ('Zadnji vezni', 'Zadnji vezni'), ('Prednji vezni', 'Prednji vezni'), ('Spic', 'Špic'), ('Levo krilo', 'Levo krilo'), ('Desno krilo', 'Desno krilo'), ('Levi bek', 'Levi bek'), ('Desni bek', 'Desni bek'), ('Stoper', 'Štoper')], default='Vezni igrač', max_length=20, null=True),
        ),
    ]

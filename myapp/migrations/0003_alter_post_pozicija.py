# Generated by Django 5.0 on 2024-11-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post_datum_rođenja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pozicija',
            field=models.CharField(blank=True, choices=[('Golman', 'Golman'), ('Zadnji vezni', 'Zadnji vezni'), ('Prednji vezni', 'Prednji vezni'), ('Spic', 'Spic'), ('Levo krilo', 'Levo krilo'), ('Desno krilo', 'Desno krilo'), ('Levi bek', 'Levi bek'), ('Desni bek', 'Desni bek'), ('Stoper', 'Stoper')], default='Vezni igrač', max_length=20, null=True),
        ),
    ]

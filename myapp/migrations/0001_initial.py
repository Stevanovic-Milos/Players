# Generated by Django 5.0 on 2024-11-12 19:21

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(blank=True, max_length=200, null=True)),
                ('prezime', models.CharField(max_length=200)),
                ('godiste', models.IntegerField(default=2000)),
                ('pozicija', models.CharField(blank=True, choices=[('Golman', 'Golman'), ('Defender', 'Defender'), ('Vezni igrač', 'Vezni igrač'), ('Napadač', 'Napadač'), ('Centarfor', 'Centarfor'), ('Centarbek', 'Centarbek'), ('Levi bek', 'Levi bek'), ('Desni bek', 'Desni bek')], default='Vezni igrač', max_length=20, null=True)),
                ('nedostaci', models.TextField()),
                ('prednosti', models.TextField()),
                ('visina', models.FloatField()),
                ('tezina', models.FloatField()),
                ('noga', models.CharField(blank=True, choices=[('Leva', 'Leva'), ('Desna', 'Desna')], max_length=5, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/posts')),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('video_url', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

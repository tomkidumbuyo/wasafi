# Generated by Django 2.0.2 on 2018-04-24 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180419_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('crewPosition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CrewPositions')),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Genres')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='SeriesGenres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Genres')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Series')),
            ],
        ),
    ]

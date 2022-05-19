# Generated by Django 3.2.12 on 2022-05-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('release_date', models.DateField()),
                ('poster_path', models.TextField()),
                ('original_title', models.CharField(max_length=100)),
                ('original_language', models.CharField(max_length=100)),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('genres_id', models.ManyToManyField(related_name='movies', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField(null=True)),
                ('imdb_id', models.CharField(max_length=100, null=True)),
                ('profile_path', models.CharField(max_length=500, null=True)),
                ('filmographies', models.ManyToManyField(related_name='actors', to='movies.Movie')),
            ],
        ),
    ]

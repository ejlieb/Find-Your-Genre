# Generated by Django 3.2.12 on 2022-05-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_rename_genres_id_movie_genres'),
        ('accounts', '0004_user_actor_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='genre_counts',
            field=models.ManyToManyField(related_name='liking_users', through='accounts.GenreCounts', to='movies.Genre'),
        ),
    ]
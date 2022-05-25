# Generated by Django 3.2.12 on 2022-05-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_provider'),
        ('accounts', '0009_user_counted_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='counted_actors',
            field=models.ManyToManyField(related_name='recorded_user', through='accounts.ActorCounts', to='movies.Actor'),
        ),
    ]
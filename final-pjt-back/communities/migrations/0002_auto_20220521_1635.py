# Generated by Django 3.2.12 on 2022-05-21 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
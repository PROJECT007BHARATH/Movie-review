# Generated by Django 4.2.10 on 2024-04-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0007_alter_movie_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Trailer',
            field=models.CharField(max_length=250),
        ),
    ]

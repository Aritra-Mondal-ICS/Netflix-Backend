# Generated by Django 4.1.7 on 2023-02-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix_backend_api', '0026_movie_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
# Generated by Django 5.1 on 2024-08-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_remove_user_favourite_movies_user_favourite_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favourite_movies',
            field=models.ManyToManyField(blank=True, related_name='users', to='personas.movie'),
        ),
    ]

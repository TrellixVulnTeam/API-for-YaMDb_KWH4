# Generated by Django 2.2.16 on 2022-06-07 19:09

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=256, verbose_name='Category_name')),
                ('slug', models.SlugField(primary_key=True, serialize=False, verbose_name='slug_name')),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(max_length=256, verbose_name='Genre_name')),
                ('slug', models.SlugField(primary_key=True, serialize=False, verbose_name='Genre_slug_name')),
            ],
            options={
                'verbose_name': 'Genre',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Title_name')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2022)], verbose_name='Year_of_production')),
                ('description', models.CharField(blank=True, max_length=256, verbose_name='Title_description')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='Title_category')),
                ('genre', models.ManyToManyField(related_name='titles', through='reviews.GenreTitle', to='reviews.Genre')),
            ],
            options={
                'verbose_name': 'Title',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.Title')),
            ],
            options={
                'unique_together': {('title', 'author')},
            },
        ),
        migrations.AddField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Title'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review')),
            ],
        ),
    ]
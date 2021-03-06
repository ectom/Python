# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-24 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_author',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_authors.Author'),
        ),
        migrations.AlterField(
            model_name='book_author',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='book_authors.Book'),
        ),
    ]

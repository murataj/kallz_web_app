# Generated by Django 3.1.1 on 2020-10-22 18:32

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kallz_app', '0004_auto_20201022_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateTimeField(null=True, verbose_name=builtins.input),
        ),
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(choices=[('Kids 8-12 years', 'Kids 8-12 years'), ('Teenagers 13-18 years old', 'Teenagers 13-18 years old'), ('Adults older than 19', 'Adults older than 19')], max_length=200, null=True),
        ),
    ]
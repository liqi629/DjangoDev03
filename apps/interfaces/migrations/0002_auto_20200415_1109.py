# Generated by Django 3.0.4 on 2020-04-15 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaces', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interfaces',
            old_name='project',
            new_name='project_id',
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id主键'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-19 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activation_code',
        ),
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=1, max_length=35, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

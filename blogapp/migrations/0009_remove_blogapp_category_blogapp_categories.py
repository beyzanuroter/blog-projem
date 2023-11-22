# Generated by Django 4.2.6 on 2023-11-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_blogapp_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogapp',
            name='category',
        ),
        migrations.AddField(
            model_name='blogapp',
            name='categories',
            field=models.ManyToManyField(to='blogapp.category'),
        ),
    ]
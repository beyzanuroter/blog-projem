# Generated by Django 4.2.6 on 2023-10-31 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_alter_blogapp_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogapp',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogapp.category'),
        ),
    ]

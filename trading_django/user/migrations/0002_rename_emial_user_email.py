# Generated by Django 4.2.2 on 2023-06-12 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='emial',
            new_name='email',
        ),
    ]

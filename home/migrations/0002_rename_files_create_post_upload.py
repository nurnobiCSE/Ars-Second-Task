# Generated by Django 4.0.4 on 2022-05-15 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='create_post',
            old_name='files',
            new_name='upload',
        ),
    ]
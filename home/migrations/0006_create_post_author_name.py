# Generated by Django 3.2.7 on 2022-05-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_registerd_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_post',
            name='author_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

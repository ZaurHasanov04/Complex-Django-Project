# Generated by Django 3.1.7 on 2021-03-10 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
    ]

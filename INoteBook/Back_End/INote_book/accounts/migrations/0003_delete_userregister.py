# Generated by Django 5.0.2 on 2024-02-12 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_user_userregister_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRegister',
        ),
    ]

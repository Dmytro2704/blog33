# Generated by Django 4.2.7 on 2023-12-12 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_profile_sign_up_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='login',
            new_name='user',
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_profile_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='poster',
            field=models.ImageField(default='https://i.pinimg.com/564x/92/c5/11/92c511eb998b41b3d6c78fc9522f5927.jpg', upload_to='uploads/', verbose_name='Poster'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_rename_com_post_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='poster',
            field=models.URLField(default='https://i.pinimg.com/564x/92/c5/11/92c511eb998b41b3d6c78fc9522f5927.jpg', verbose_name='Постер'),
        ),
    ]

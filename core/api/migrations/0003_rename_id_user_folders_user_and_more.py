# Generated by Django 4.0.4 on 2022-05-25 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_folders_id_user_alter_items_id_folders_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folders',
            old_name='id_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='id_user',
            new_name='user',
        ),
    ]

# Generated by Django 3.2.16 on 2022-12-23 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='staff',
            new_name='is_staff',
        ),
    ]
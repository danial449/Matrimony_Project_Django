# Generated by Django 4.2.7 on 2023-11-25 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_email_verification_token_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_email_verification_token',
            new_name='email_verification_token',
        ),
    ]

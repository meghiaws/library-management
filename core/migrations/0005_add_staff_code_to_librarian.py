# Generated by Django 3.2.13 on 2022-06-03 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_add_membership_code_to_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='staff_code',
            field=models.CharField(default="0000000", max_length=7),
            preserve_default=False,
        ),
    ]
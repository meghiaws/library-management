# Generated by Django 3.2.13 on 2022-06-04 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('library', '0007_change_max_length_to_8'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='borrower',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.member'),
        ),
        migrations.DeleteModel(
            name='Librarian',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
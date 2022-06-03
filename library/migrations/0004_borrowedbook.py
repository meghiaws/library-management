# Generated by Django 3.2.13 on 2022-06-03 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_member'),
        ('library', '0003_bookitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateField(auto_now=True)),
                ('due_date', models.DateField()),
                ('book_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.bookitem')),
                ('borrower', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.member')),
            ],
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-02 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=15, unique=True)),
                ('status', models.CharField(choices=[('A', 'Available'), ('B', 'Borrow'), ('R', 'Reserved'), ('L', 'Lost')], max_length=1)),
                ('publication_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]

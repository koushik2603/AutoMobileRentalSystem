# Generated by Django 4.1.7 on 2023-03-30 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('registrationtime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'registration_table',
            },
        ),
    ]

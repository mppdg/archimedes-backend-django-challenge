# Generated by Django 4.0.2 on 2022-02-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('User', 'User'), ('Admin', 'Admin')], default='User', max_length=5)),
            ],
        ),
    ]

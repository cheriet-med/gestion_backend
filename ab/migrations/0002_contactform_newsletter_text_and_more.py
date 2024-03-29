# Generated by Django 4.2.2 on 2023-06-16 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10000, null=True)),
                ('email', models.CharField(blank=True, max_length=10000, null=True)),
                ('subject', models.CharField(blank=True, max_length=10000, null=True)),
                ('message', models.CharField(blank=True, max_length=10000, null=True)),
                ('date', models.CharField(blank=True, max_length=10000, null=True)),
                ('time', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=10000, null=True)),
                ('date', models.CharField(blank=True, max_length=10000, null=True)),
                ('time', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10000, null=True)),
                ('text_en', models.CharField(blank=True, max_length=10000, null=True)),
                ('text_fr', models.CharField(blank=True, max_length=10000, null=True)),
                ('text_ar', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('last_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('adress', models.CharField(blank=True, max_length=1000, null=True)),
                ('city', models.CharField(blank=True, max_length=1000, null=True)),
                ('province', models.CharField(blank=True, max_length=1000, null=True)),
                ('country', models.CharField(blank=True, max_length=1000, null=True)),
                ('phone', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand', models.CharField(blank=True, max_length=1000, null=True)),
                ('theme', models.CharField(blank=True, max_length=1000, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('password', models.CharField(blank=True, max_length=1000, null=True)),
                ('username', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.CharField(blank=True, max_length=1000, null=True)),
                ('time', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.CharField(blank=True, max_length=1000, null=True)),
                ('domain', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sizelist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

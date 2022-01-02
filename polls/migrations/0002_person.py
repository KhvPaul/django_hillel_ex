# Generated by Django 4.0 on 2021-12-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, help_text='Enter person first name', max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, help_text='Enter person last name', max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, help_text='Enter person email', max_length=254, verbose_name='email address')),
            ],
        ),
    ]
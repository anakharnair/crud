# Generated by Django 4.1.2 on 2023-03-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('adress', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='')),
                ('desig', models.CharField(max_length=250)),
            ],
        ),
    ]
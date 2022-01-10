# Generated by Django 4.0.1 on 2022-01-10 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('category', models.TextField()),
                ('video', models.TextField()),
                ('calories_food', models.TextField()),
                ('cooking_time', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

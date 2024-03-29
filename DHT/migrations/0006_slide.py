# Generated by Django 5.0 on 2024-01-05 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHT', '0005_member_remove_registry_author_delete_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='slides/')),
            ],
        ),
    ]

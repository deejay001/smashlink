# Generated by Django 3.0.8 on 2020-10-30 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-updated_on']},
        ),
    ]

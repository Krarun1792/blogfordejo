# Generated by Django 2.2.5 on 2020-05-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
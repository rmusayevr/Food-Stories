# Generated by Django 4.0.6 on 2022-09-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
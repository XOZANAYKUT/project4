# Generated by Django 4.2.11 on 2024-03-22 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_comment_reply_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply_body',
        ),
    ]

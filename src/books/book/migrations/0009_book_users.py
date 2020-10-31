# Generated by Django 2.2.16 on 2020-10-28 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_phone'),
        ('book', '0008_remove_book_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.User'),
            preserve_default=False,
        ),
    ]

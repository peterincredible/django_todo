# Generated by Django 3.0.3 on 2020-03-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytodos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytodosmodel',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='mytodosmodel',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.2 on 2023-04-22 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0004_alter_course_difficulty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="comment",
            field=models.TextField(verbose_name="comment"),
        ),
    ]

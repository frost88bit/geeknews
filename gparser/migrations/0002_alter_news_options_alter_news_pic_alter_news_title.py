# Generated by Django 4.1.6 on 2023-02-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gparser", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name": "News", "verbose_name_plural": "All_News"},
        ),
        migrations.AlterField(
            model_name="news",
            name="pic",
            field=models.URLField(max_length=250, verbose_name="Pic_link"),
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(max_length=300, verbose_name="Title"),
        ),
    ]

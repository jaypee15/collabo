# Generated by Django 4.2.6 on 2023-10-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_bio_user_is_open_to_collab_user_linkedin_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, max_length=100, verbose_name="Username of User"),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="discription",
            name="dics_image",
            field=models.ImageField(
                default="-",
                height_field="300",
                upload_to="aboutç_img",
                width_field="200",
            ),
        ),
    ]
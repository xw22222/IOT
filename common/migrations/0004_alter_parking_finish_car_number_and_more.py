# Generated by Django 4.1.1 on 2023-02-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_alter_parking_parking_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parking",
            name="finish_car_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="parking",
            name="parking_car_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

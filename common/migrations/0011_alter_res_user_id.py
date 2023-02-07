# Generated by Django 4.1.1 on 2023-02-05 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0010_alter_res_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="res",
            name="user_id",
            field=models.ForeignKey(
                blank=True,
                db_column="user_id",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
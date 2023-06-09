# Generated by Django 4.2 on 2023-04-13 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_checkmodel_client"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkmodel",
            name="client",
            field=models.ForeignKey(
                db_constraint=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="checks",
                to="app.clientmodel",
            ),
        ),
    ]

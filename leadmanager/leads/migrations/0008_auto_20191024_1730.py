# Generated by Django 2.2.5 on 2019-10-24 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_remove_project_is_dot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

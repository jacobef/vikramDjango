# Generated by Django 4.0.5 on 2022-06-10 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminApp', '0002_rename_messagemod_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='To',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Recipiant',
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-21 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModelTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('something', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputField', models.TextField(max_length=100000000000000000000)),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to=settings.AUTH_USER_MODEL)),
                ('To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bool_example', models.BooleanField()),
                ('small_text_example', models.CharField(max_length=100)),
                ('large_text_example', models.TextField(max_length=1000)),
                ('example_other_model_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.examplemodeltwo')),
            ],
        ),
    ]

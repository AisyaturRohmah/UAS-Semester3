# Generated by Django 4.0.5 on 2022-12-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hijab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warna', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
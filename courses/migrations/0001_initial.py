# Generated by Django 4.2.10 on 2024-04-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('url', models.URLField()),
                ('preview', models.ImageField(default='default_courses', upload_to='course_preview')),
            ],
        ),
    ]
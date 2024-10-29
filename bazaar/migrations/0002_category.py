# Generated by Django 3.0.5 on 2021-11-28 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('englishname', models.CharField(max_length=300)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/categories/')),
            ],
        ),
    ]

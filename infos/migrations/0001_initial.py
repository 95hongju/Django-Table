# Generated by Django 2.1.3 on 2018-11-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode_num', models.CharField(max_length=30)),
                ('freeze_num', models.CharField(max_length=10)),
                ('box_num', models.CharField(max_length=10)),
                ('rack_num', models.CharField(max_length=10)),
                ('well_num', models.CharField(max_length=10)),
            ],
        ),
    ]
# Generated by Django 3.2.23 on 2023-12-08 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('emp_code', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(default='', upload_to='uploads/images')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.position')),
            ],
        ),
    ]

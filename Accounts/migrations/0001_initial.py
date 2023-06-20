# Generated by Django 4.2 on 2023-06-20 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(blank=True, choices=[('school', 'Школа'), ('kg', 'Детский сад')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('role', models.TextField(choices=[('admin', 'Администратор'), ('teacher', 'Учитель'), ('parent', 'Родитель'), ('student', 'Ученик'), ('methodist', 'Методист')], max_length=10, null=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('second_name', models.CharField(max_length=50, null=True)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_of_birth', models.DateField(null=True, verbose_name='дата рождения')),
                ('points', models.IntegerField(default=0)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.building')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

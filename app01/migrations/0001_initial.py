# Generated by Django 4.1.1 on 2022-09-13 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='depatment_title')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='user_name')),
                ('password', models.CharField(max_length=64, verbose_name='pwd')),
                ('age', models.IntegerField(verbose_name='age')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='salary')),
                ('create_time', models.DateTimeField(verbose_name='create_time')),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'divers')])),
                ('depart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department')),
            ],
        ),
    ]

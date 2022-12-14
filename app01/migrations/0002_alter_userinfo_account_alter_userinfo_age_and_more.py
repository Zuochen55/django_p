# Generated by Django 4.1.1 on 2022-09-18 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='account',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Account'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='Create time'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='depart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'divers')], verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=32, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=64, verbose_name='Password'),
        ),
    ]

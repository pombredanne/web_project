# Generated by Django 2.0.7 on 2018-08-21 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=512)),
                ('eng_name', models.CharField(max_length=512)),
                ('cn_name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='DestInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_showname', models.CharField(max_length=512)),
                ('dest_abbreviation', models.CharField(max_length=16)),
                ('dest_introduce', models.TextField()),
                ('country_list', models.ManyToManyField(to='testmanage.CountryInfo')),
            ],
        ),
        migrations.CreateModel(
            name='FieldInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=512)),
                ('field_type', models.CharField(max_length=512)),
                ('field_show_when_execute', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FieldOptionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_value', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='KeywordInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='ModelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=512)),
                ('model_intro', models.CharField(max_length=512)),
                ('user_name', models.CharField(max_length=64)),
                ('charger', models.CharField(max_length=64)),
                ('create_datetime', models.CharField(max_length=32)),
                ('update_datetime', models.CharField(max_length=32)),
                ('parent_model', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ProjInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_name', models.CharField(max_length=512)),
                ('proj_intro', models.CharField(max_length=512)),
                ('user_name', models.CharField(max_length=64)),
                ('charger', models.CharField(max_length=64)),
                ('create_datetime', models.CharField(max_length=32)),
                ('update_datetime', models.CharField(max_length=32)),
                ('is_catus', models.BooleanField()),
                ('dest_list', models.ManyToManyField(to='testmanage.DestInfo')),
                ('option_field_list', models.ManyToManyField(to='testmanage.FieldInfo')),
            ],
        ),
        migrations.AddField(
            model_name='modelinfo',
            name='parent_proj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmanage.ProjInfo'),
        ),
        migrations.AddField(
            model_name='fieldinfo',
            name='field_option_list',
            field=models.ManyToManyField(to='testmanage.FieldOptionInfo'),
        ),
    ]
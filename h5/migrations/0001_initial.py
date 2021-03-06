# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='H5TestCase1',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('action', models.CharField(max_length=45, null=True)),
                ('value', models.TextField(null=True)),
                ('expected', models.TextField(null=True)),
                ('actual', models.TextField(editable=False, null=True)),
                ('result', models.CharField(editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'h_animal_project_released',
                'verbose_name': '\u52a8\u7269\u4fdd\u62a4\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': '\u52a8\u7269\u4fdd\u62a4\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='H5TestCase2',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('action', models.CharField(max_length=45, null=True)),
                ('value', models.TextField(null=True)),
                ('expected', models.TextField(null=True)),
                ('actual', models.TextField(editable=False, null=True)),
                ('result', models.CharField(editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'h_disaster_project_released',
                'verbose_name': '\u5927\u75c5\u6551\u52a9\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': '\u5927\u75c5\u6551\u52a9\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='H5TestCase3',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('action', models.CharField(max_length=45, null=True)),
                ('value', models.TextField(null=True)),
                ('expected', models.TextField(null=True)),
                ('actual', models.TextField(editable=False, null=True)),
                ('result', models.CharField(editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'h_dream_project_released',
                'verbose_name': '\u68a6\u60f3\u6e05\u5355\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': '\u68a6\u60f3\u6e05\u5355\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='H5TestCase4',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('action', models.CharField(max_length=45, null=True)),
                ('value', models.TextField(null=True)),
                ('expected', models.TextField(null=True)),
                ('actual', models.TextField(editable=False, null=True)),
                ('result', models.CharField(editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'h_illness_project_released',
                'verbose_name': '\u5927\u75c5\u6551\u52a9\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': '\u5927\u75c5\u6551\u52a9\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='H5TestCase5',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('action', models.CharField(max_length=45, null=True)),
                ('value', models.TextField(null=True)),
                ('expected', models.TextField(null=True)),
                ('actual', models.TextField(editable=False, null=True)),
                ('result', models.CharField(editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'h_poverty_project_released',
                'verbose_name': '\u6276\u8d2b\u52a9\u5b66\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': '\u6276\u8d2b\u52a9\u5b66\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='H5TestCase6',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('action', models.CharField(max_length=45, null=True)),
                ('value', models.TextField(null=True)),
                ('expected', models.TextField(null=True)),
                ('actual', models.TextField(editable=False, null=True)),
                ('result', models.CharField(editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'h_presale_project_released',
                'verbose_name': '\u5c1d\u9c9c\u9884\u552e\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': '\u5c1d\u9c9c\u9884\u552e\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='H5TestCase7',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('action', models.CharField(max_length=45, null=True)),
                ('value', models.TextField(null=True)),
                ('expected', models.TextField(null=True)),
                ('actual', models.TextField(editable=False, null=True)),
                ('result', models.CharField(editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'h_other_project_released',
                'verbose_name': '\u5176\u5b83\u9879\u76ee\u53d1\u5e03',
                'verbose_name_plural': '\u5176\u5b83\u9879\u76ee\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='H5TestCase8',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('action', models.CharField(max_length=45, null=True)),
                ('value', models.TextField(null=True)),
                ('expected', models.TextField(null=True)),
                ('actual', models.TextField(editable=False, null=True)),
                ('result', models.CharField(editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'h_support_project',
                'verbose_name': '\u652f\u6301\u5df2\u521b\u5efa\u7684\u9879\u76ee',
                'verbose_name_plural': '\u652f\u6301\u5df2\u521b\u5efa\u7684\u9879\u76ee',
            },
        ),
        migrations.CreateModel(
            name='H5TestCase9',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=45)),
                ('case_name', models.CharField(max_length=45)),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('action', models.CharField(max_length=45, null=True)),
                ('value', models.TextField(null=True)),
                ('expected', models.TextField(null=True)),
                ('actual', models.TextField(editable=False, null=True)),
                ('result', models.CharField(editable=False, max_length=5, null=True)),
                ('state', models.IntegerField(default='1')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'h_check_project',
                'verbose_name': '\u67e5\u770b\u4e2a\u4eba\u9879\u76ee',
                'verbose_name_plural': '\u67e5\u770b\u4e2a\u4eba\u9879\u76ee',
            },
        ),
    ]

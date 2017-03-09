# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 12:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('description', models.TextField()),
                ('spentTime', models.TimeField()),
                ('donePercentage', models.PositiveIntegerField()),
                ('assignedTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignedIssues', to=settings.AUTH_USER_MODEL)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdIssues', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=10, unique=True)),
                ('marker', models.CharField(choices=[('default', 'silver'), ('primary', 'blue'), ('success', 'green'), ('info', 'light blue'), ('warning', 'yellow'), ('danger', 'red')], default='default', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('contributors', models.ManyToManyField(blank=True, related_name='contributors', to=settings.AUTH_USER_MODEL)),
                ('project_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoleOnProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('administrator', 'admin'), ('programmer', 'developer'), ('quality assurance', 'qa')], max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='app.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roleOnProject', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=10, unique=True)),
                ('marker', models.CharField(choices=[('default', 'silver'), ('primary', 'blue'), ('success', 'green'), ('info', 'light blue'), ('warning', 'yellow'), ('danger', 'red')], default='default', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('historyitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.HistoryItem')),
                ('message', models.TextField()),
            ],
            bases=('app.historyitem',),
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('historyitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.HistoryItem')),
                ('link', models.URLField()),
            ],
            bases=('app.historyitem',),
        ),
        migrations.CreateModel(
            name='IssueChange',
            fields=[
                ('historyitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.HistoryItem')),
                ('propertyName', models.CharField(max_length=50)),
                ('oldValue', models.CharField(max_length=50)),
                ('newValue', models.CharField(max_length=50)),
            ],
            bases=('app.historyitem',),
        ),
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Priority'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Project'),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Status'),
        ),
        migrations.AddField(
            model_name='historyitem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historyItem', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historyitem',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historyItemIssue', to='app.Issue'),
        ),
    ]

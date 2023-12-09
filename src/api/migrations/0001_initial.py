# Generated by Django 5.0 on 2023-12-09 16:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'graph',
                'db_table_comment': 'Contains information about a graph',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=256)),
                ('has_header', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'source',
                'db_table_comment': 'Describes the location of CSV data.',
            },
        ),
        migrations.CreateModel(
            name='GraphDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_type', models.CharField(choices=[('line', 'line'), ('bar', 'bar')], max_length=16)),
                ('label', models.CharField(max_length=128)),
                ('is_axis', models.BooleanField(default=False)),
                ('column', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.graph')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.source')),
            ],
            options={
                'db_table': 'graph_dataset',
                'db_table_comment': 'Describes individual datasets that can be plotted to a graph',
            },
        ),
        migrations.CreateModel(
            name='SourceColumnConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('column_name', models.CharField(max_length=128)),
                ('transform_name', models.CharField(choices=[('none', '')], default='none', max_length=128)),
                ('unit', models.CharField(max_length=32)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.source')),
            ],
            options={
                'db_table': 'source_column_config',
                'db_table_comment': 'Contains configuration for individual columns of data-sources.',
            },
        ),
    ]

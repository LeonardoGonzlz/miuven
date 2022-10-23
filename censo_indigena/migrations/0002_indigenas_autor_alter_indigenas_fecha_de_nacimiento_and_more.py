# Generated by Django 4.1.2 on 2022-10-20 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('censo_indigena', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indigenas',
            name='autor',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indigenas',
            name='fecha_de_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='indigenas',
            name='grado_instruccion',
            field=models.CharField(max_length=14),
        ),
        migrations.CreateModel(
            name='Historicalindigenas',
            fields=[
                ('cedula', models.CharField(db_index=True, max_length=11)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('etnia', models.CharField(max_length=30)),
                ('casta', models.CharField(max_length=30)),
                ('grado_instruccion', models.CharField(max_length=14)),
                ('fecha_de_nacimiento', models.DateField()),
                ('estado_de_salud', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=12)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('autor', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical censo de indigena',
                'verbose_name_plural': 'historical censo de indigenas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]

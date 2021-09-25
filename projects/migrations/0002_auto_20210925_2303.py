# Generated by Django 3.2.7 on 2021-09-25 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(verbose_name='Date created')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='label',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_uuid', models.CharField(max_length=255)),
                ('is_selected', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(verbose_name='Date created')),
                ('modified_date', models.DateTimeField(verbose_name='Date modified')),
                ('funnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.funnel')),
            ],
        ),
        migrations.AddField(
            model_name='funnel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
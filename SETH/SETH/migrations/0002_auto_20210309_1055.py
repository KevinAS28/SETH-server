# Generated by Django 3.1.7 on 2021-03-09 10:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SETH', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='a_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SETH.aplace'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='note',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='aplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aplace', to='SETH.aplace'),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='bday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='bplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bplace', to='SETH.bplace'),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='face_data',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='fingerprint',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='nik',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='password',
            field=models.CharField(blank=True, default='12345', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='postalcode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonuser',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='history',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]

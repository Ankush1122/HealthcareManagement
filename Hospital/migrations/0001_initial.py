# Generated by Django 5.1.1 on 2024-09-30 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=10)),
                ('details', models.TextField()),
                ('entity', models.ForeignKey(limit_choices_to={'role__in': ['Doctor', 'Pharmacist', 'Pathologist']}, on_delete=django.db.models.deletion.CASCADE, to='User.user')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('visit_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_visit', models.DateTimeField()),
                ('visit_type', models.CharField(choices=[('Doctor', 'Doctor'), ('Pharmacist', 'Pharmacist'), ('Pathologist', 'Pathologist')], max_length=20)),
                ('bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hospital.bill')),
                ('entity', models.ForeignKey(limit_choices_to={'role__in': ['Doctor', 'Pharmacist', 'Pathologist']}, on_delete=django.db.models.deletion.CASCADE, to='User.user')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.patient')),
            ],
        ),
    ]
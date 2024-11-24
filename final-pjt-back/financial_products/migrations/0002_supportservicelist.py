# Generated by Django 4.2.16 on 2024-11-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportServiceList',
            fields=[
                ('service_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('support_type', models.CharField(max_length=100)),
                ('service_nm', models.CharField(max_length=200)),
                ('service_pur', models.TextField()),
                ('eligibility', models.TextField()),
                ('selection_criteria', models.TextField()),
                ('support_details', models.TextField()),
                ('application_method', models.TextField()),
                ('application_deadline', models.CharField(blank=True, max_length=100, null=True)),
                ('detail_url', models.URLField()),
                ('agency_code', models.CharField(max_length=50)),
                ('agency_name', models.CharField(max_length=200)),
                ('part_nm', models.CharField(blank=True, max_length=200, null=True)),
                ('agency_type', models.CharField(max_length=100)),
                ('user_class', models.CharField(max_length=100)),
                ('service_class', models.CharField(max_length=100)),
                ('reception_agency', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-21 05:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('createOrder', '0002_auto_20211120_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(blank=True, default=datetime.datetime.today)),
                ('customer_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='createOrder.customer', verbose_name='Customer ID')),
                ('employee_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='createOrder.employee', verbose_name='Employee ID')),
            ],
            options={
                'db_table': 'job_order',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category_name', models.CharField(max_length=50)),
                ('product_category_description', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'product_cateogory',
            },
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed_date', models.DateTimeField(blank=True, default=datetime.datetime.today)),
                ('status', models.CharField(max_length=15)),
                ('status_change_date', models.DateTimeField(blank=True, default=datetime.datetime.today)),
                ('filing_cabinet', models.CharField(max_length=10)),
                ('file_name', models.CharField(max_length=25)),
                ('notes', models.CharField(max_length=500)),
                ('employee_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='createOrder.employee', verbose_name='Employee ID')),
                ('order_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='createOrder.job_order', verbose_name='Order ID')),
                ('product_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='createOrder.product', verbose_name='Product ID')),
            ],
            options={
                'db_table': 'ticket',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_category_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='createOrder.product_category', verbose_name='Product Category ID'),
        ),
        migrations.CreateModel(
            name='order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('quoted_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_notes', models.CharField(max_length=500)),
                ('product_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='createOrder.product', verbose_name='Product ID')),
            ],
            options={
                'db_table': 'order_detail',
            },
        ),
    ]

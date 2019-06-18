# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-18 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('comment', models.TextField(default='', verbose_name='评价信息')),
                ('score', models.SmallIntegerField(default=5, verbose_name='满意度评分')),
                ('is_anonymous', models.BooleanField(default=False, verbose_name='是否匿名评价')),
                ('is_commented', models.BooleanField(default=False, verbose_name='是否评价了')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
                'db_table': 'tb_order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('order_id', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='订单号')),
                ('total_count', models.IntegerField(default=1, verbose_name='商品总数')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品总金额')),
                ('freight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='运费')),
                ('pay_method', models.SmallIntegerField(default=1, verbose_name='支付方式')),
                ('status', models.SmallIntegerField(default=1, verbose_name='订单状态')),
            ],
            options={
                'verbose_name': '订单基本信息',
                'verbose_name_plural': '订单基本信息',
                'db_table': 'tb_order_info',
            },
        ),
    ]

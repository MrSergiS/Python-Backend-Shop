# Generated by Django 5.1.7 on 2025-03-31 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops_backend', '0002_goods_goodscomment_goodsimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsimg',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shops_backend.goods'),
        ),
    ]

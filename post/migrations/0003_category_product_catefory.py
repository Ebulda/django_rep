# Generated by Django 4.2.7 on 2023-12-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='catefory',
            field=models.ManyToManyField(blank=True, related_name='products', to='post.category'),
        ),
    ]

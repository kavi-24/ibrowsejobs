# Generated by Django 4.2.4 on 2023-08-20 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_course_coursecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='coupon_code',
            field=models.CharField(default='_', max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='coupon_disc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='discounted_price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='UsedCoupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mysite.student')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-21 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_personnel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.personnel')),
            ],
        ),
    ]

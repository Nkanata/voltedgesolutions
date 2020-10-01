# Generated by Django 2.2.4 on 2019-10-06 18:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('VoltsBackEnd', '0006_product_product_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_or_person', models.CharField(choices=[('O', 'Organisation'), ('P', 'Person')], default='PERSON', max_length=2)),
                ('organisation_name', models.CharField(blank=True, max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.PositiveSmallIntegerField(verbose_name='Phone Number')),
                ('address_line_1', models.CharField(max_length=100, verbose_name='Address 1')),
                ('address_line_2', models.CharField(blank=True, max_length=100)),
                ('town_city', models.CharField(max_length=50, verbose_name='City or Town')),
                ('county', models.CharField(max_length=20, verbose_name='County')),
                ('country', models.CharField(max_length=20, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_item_quantity', models.PositiveSmallIntegerField()),
                ('order_item_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('RMA_number', models.PositiveSmallIntegerField(blank=True)),
                ('RMA_issued_by', models.CharField(blank=True, max_length=50)),
                ('RMA_issued_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=15)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='RefInvoiceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_status', models.CharField(max_length=15)),
                ('invoice_status_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RefOrderItemStatusCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_item_status_code', models.CharField(max_length=10)),
                ('order_item_status_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RefOrderStatusCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status_code', models.PositiveSmallIntegerField()),
                ('order_status_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_date', models.DateField(auto_now_add=True)),
                ('shipment_tracking_number', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('invoice_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VoltsBackEnd.Invoice')),
            ],
        ),
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_buyer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_ship_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_shipped',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_shipping_fee',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_tax',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_tracking_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='date_order_placed',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_customer_instruction',
            field=models.TextField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='product',
            name='return_merchandise_authorization_nr',
            field=models.IntegerField(default=0, verbose_name='code to authorize return of a product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='productoption',
            name='product_price_decrement',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='productoption',
            name='product_price_increment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.AddField(
            model_name='shipment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_shipment', to='VoltsBackEnd.Order'),
        ),
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderPayment', to='VoltsBackEnd.Order'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderItems', to='VoltsBackEnd.Order'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='VoltsBackEnd.Product'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceStatus', to='VoltsBackEnd.RefInvoiceStatus'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='VoltsBackEnd.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='CustomerOrder', to='VoltsBackEnd.Customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_status_Code',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='orderStatus', to='VoltsBackEnd.RefOrderStatusCodes'),
            preserve_default=False,
        ),
    ]

from VoltsBackEnd.models import Order
from django.db import models


# Create your models here.

class MpesaPaymentOrder(models.Model):
    TransID = models.CharField(max_length=20)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="MpesaOrders"
    )
    payment_time = models.DateTimeField(auto_now_add=True)
    TransTime = models.CharField(max_length=30, verbose_name="The time mpesa received payment")
    MSISDN = models.PositiveIntegerField()
    TransAmount = models.DecimalField(max_digits=8, decimal_places=2)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30, blank=True)
    MiddleName = models.CharField(max_length=30)


class MpesaPaymentUnKnownOrder(models.Model):
    TransID = models.CharField(max_length=20)
    BillRefNumber = models.CharField(max_length=20)
    payment_time = models.DateTimeField(auto_now_add=True)
    TransTime = models.CharField(max_length=30, verbose_name="The time mpesa received payment")
    MSISDN = models.PositiveIntegerField()
    TransAmount = models.DecimalField(max_digits=8, decimal_places=2)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30, blank=True)
    MiddleName = models.CharField(max_length=30)
    validated = models.BooleanField(default=False)

from rest_framework import serializers
from .models import MpesaPaymentOrder, MpesaPaymentUnKnownOrder


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaPaymentOrder
        exclude = ['payment_time']


class UnknownPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaPaymentUnKnownOrder
        exclude = ['validated']

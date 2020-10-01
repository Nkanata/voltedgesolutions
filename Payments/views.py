# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import BasePermission
from Payments.serializers import PaymentSerializer, UnknownPaymentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.response import Response
from VoltsBackEnd.models import Order
from django.core.exceptions import ObjectDoesNotExist
from .tasks import payment_confirmed, payment_processed


# Create your views here.
class PaymentPermission(BasePermission):
    def has_permission(self, request, view):
        api_url = "sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
        if request.META['REMOTE_HOST'] == api_url:
            return True
        return False


accept_resp = {
    "ResultCode": 0,
    "ResultDesc": "Accepted"
}


@renderer_classes([JSONRenderer])
@api_view(['POST'])
# @permission_classes([PaymentPermission])
def validator(request):
    reject_resp = {
        "ResultCode": 1,
        "ResultDesc": "Rejected"
    }
    try:
        Order.objects.get(order_id__istartswith=request.data.get('BillRefNumber'))
    except ObjectDoesNotExist:
        return Response(reject_resp)

    return Response(accept_resp)


@renderer_classes([JSONRenderer])
@api_view(['POST'])
# @permission_classes([PaymentPermission])
def confirm(request):
    # check remote address making confirmation
    global order
    order_id = request.data.get('BillRefNumber')
    try:
        order = Order.objects.get(order_id__istartswith=request.data.get('BillRefNumber'))
    except ObjectDoesNotExist:
        unknownpay = UnknownPaymentSerializer(data=request.data)
        if unknownpay.is_valid():
            unknownpay.save()
            return Response(unknownpay.validated_data)
    if float(request.data.get('TransAmount')) >= order.get_total_cost():
        order.paid = True
        order.save(update_fields=['paid'])
        payment_processed.delay(order_id)
    order_dict = {"order": order.order_id}
    data2 = request.data
    data2.update(order_dict)
    trans_amount = request.data.get('TransAmount')
    pay_serializer = PaymentSerializer(data=data2)
    # pay_serializer = PaymentSerializer(data=request.data)
    pay_serializer.is_valid()
    if pay_serializer.is_valid():
        pay_serializer.save()
        # payment confirmation task here pass order and trans amount received
        payment_confirmed.delay(order_id, trans_amount)
        # return Response(pay_serializer.data)
        return Response("{}".format(request.META.get('REMOTE_ADDR')))

    # return Response(pay_serializer.validated_data)
    # return Response(data2)

# class Confirm(generics.CreateAPIView):
#   serializer_class = PaymentSerializer(partial=True)
#    name = 'confirm'

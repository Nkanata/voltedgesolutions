from celery import task
from django.core.mail import send_mail
from VoltsBackEnd.models import Order


@task
def payment_confirmed(order_id, trans_amount):
    order = Order.objects.get(order_id__istartswith=order_id)
    ord_noo = format(order.order_id).split('-')[0]
    first_name = order.customer.first_name
    # total = order.get_total_cost()
    subject = 'Payment Successful for Order {}'.format(ord_noo)
    # subject = 'Payment Successful for Order. {}'.format(order.order_id).split('-')[0]
    message = 'Dear {},\n\n Your Payment of KShs. {} through M-Pesa for Order {}, has been received ' \
              '\n\n Thank You. ' \
              '\n\n Your Order will be processed Shortly.' \
        .format(first_name, trans_amount, ord_noo)
    mail_sent = send_mail(subject,
                          message,
                          'admin@voltedgeshop.com',
                          [order.customer.email])
    return mail_sent


@task
def payment_processed(order_id):
    order = Order.objects.get(order_id__istartswith=order_id)
    ord_noo = format(order.order_id).split('-')[0]
    first_name = order.customer.first_name
    subject = 'Order {} '.format(ord_noo)
    message = 'Dear {},\n\nYour Order {} has been processed Successfully. We will get back to you when your order has '\
              'been Shipped.' \
        .format(first_name, ord_noo)
    mail_sent = send_mail(subject,
                          message,
                          'admin@voltedgeshop.com',
                          [order.customer.email])
    return mail_sent

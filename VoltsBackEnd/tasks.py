from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(ord_id, **args):
    order = Order.objects.get(order_id=ord_id)
    ord_no = format(order.order_id).split('-')[0]
    first_name = order.customer.first_name
    total = order.get_total_cost()
    # subject = 'Order nr. {}'.format(ord_no)
    subject = 'Order nr. {}'.format(order.order_id).split('-')[0]
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}. \n\n The total price is {}. ' \
              '\n\n Pay using our PayBill no. xxxxxx.\n\n Account no. : {}.'.format(first_name, ord_no, total, ord_no)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.customer.email])
    return mail_sent

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Robot
from orders.models import Order
from django.core.mail import send_mail


@receiver(post_save, sender=Robot)
def notify_customers_when_robot_created(sender, instance, created, **kwargs):
    if created:
        pending_orders = Order.objects.filter(robot_serial=instance.serial)
        for order in pending_orders:
            customer_email = order.customer.email
            send_mail(
                subject='Ваш робот в наличии',
                message=(
                    f"Добрый день!\n"
                    f"Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\n"
                    f"Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
                ),
            from_email = "r4c@robots.com",
            recipient_list = [customer_email],
            fail_silently = False,
            )
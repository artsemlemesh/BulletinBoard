from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DisposableCode
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from django.dispatch import Signal

# @receiver(post_save, sender=DisposableCode)
# def send_confirmation_email(sender, instance, created, **kwargs):
#     if created:
#         print('send_confirmation_email SIGNAL')
#         user = instance.user
#         confirmation_code = instance.code
#         subject = 'Account confirmation email'
#         message = f'Hello {user.username}, \n\nPlease confirm your registration by clicking the following link:\n\nhttps://yourdomain.com/confirm/{confirmation_code}'
#         send_mail(subject, message, ['artsemlemesh@yandex.by'], [user.email])

# @receiver(post_save, sender=DisposableCode)
# def expire_disposable_code(sender, instance, **kwargs):
#     instance.expires_at = timezone.now() + timedelta(minutes=1)
#     instance.save()


# disposable_code_created = Signal()
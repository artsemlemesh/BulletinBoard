from django.db.models.signals import post_save
from django.dispatch import receiver

from Board import settings
from .models import DisposableCode, Comment
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import m2m_changed

@receiver(post_save, sender=Comment)
def notify_about_comment(sender, instance, created, **kwargs):
    if created:
        print('notify about comment signal')
        author = instance.post.author.user
        post = instance.post
        text = instance.text
        subject = 'new comment'
        message = f'hello /{author.username}/, here is a comment:: /{text}/ for your post:: /{post}/'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [author.email])



@receiver(post_save, sender=Comment)
def notify_on_comment_acceptance(sender, instance, created, **kwargs):
    old_status = Comment.objects.get(pk=instance.pk).status
    if not old_status and instance.status == False:
        return
    print('notify_on_comment_acceptance')
    sender = settings.DEFAULT_FROM_EMAIL #something is wrong here, it sends and received by the same person
    recipient = instance.author.user.email

    send_notification(sender, [recipient], instance)

def send_notification(sender, recipient, comment):
    email_subject = 'Comment accepted'
    print('send_notification')
    email_message = f'your comment of the post {comment.text} has been accepted'
    send_mail(email_subject, email_message, sender, [recipient])

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
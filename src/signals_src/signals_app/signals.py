from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.contrib.auth.models import User
import threading

# Question 1: Are Django signals executed synchronously or asynchronously?
@receiver(post_save, sender=User)
def sync_signal(sender, instance, created, **kwargs):
    print("Signal executed synchronously. User saved:", instance.username)

# Question 2: Do Django signals run in the same thread as the caller?
@receiver(post_save, sender=User)
def check_thread(sender, instance, created, **kwargs):
    print("Current thread ID:", threading.get_ident())
    print("Signal runs in the same thread as the caller.")

# Question 3: Do Django signals run in the same transaction as the caller?
@receiver(post_save, sender=User)
def check_transaction(sender, instance, created, **kwargs):
    with transaction.atomic():
        print("Signal is in the same transaction as the caller.")

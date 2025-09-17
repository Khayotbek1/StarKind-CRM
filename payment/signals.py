from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Payment


def update_child_balance(child):
    """Bolaga tegishli barcha to‘lovlardan qarzdorlikni hisoblash"""
    if not child:
        return
    total_due = sum(p.amount_due for p in child.payments.all())
    total_paid = sum(p.amount_paid for p in child.payments.all())
    child.balance = total_due - total_paid
    child.save(update_fields=["balance"])


@receiver(post_save, sender=Payment)
def update_balance_after_save(sender, instance, **kwargs):
    update_child_balance(instance.child)


@receiver(post_delete, sender=Payment)
def update_balance_after_delete(sender, instance, **kwargs):
    update_child_balance(instance.child)

from random import randint
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save 
from django.dispatch import receiver
from library.models import Member


@receiver(post_save, sender=get_user_model())
def create_member_for_new_user(sender, **kwargs):
    if kwargs["created"]:
        user = kwargs["instance"]
        membership_code = str(randint(10_000_000, 99_000_000)) 
        Member.objects.create(user=user, membership_code=membership_code)

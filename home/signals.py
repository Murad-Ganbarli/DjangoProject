from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(user_logged_in)
def create_user(sender, request, user, **kwargs):
    UserModel = get_user_model()
    if not UserModel.objects.filter(pk=user.pk).exists():
        new_user = UserModel.objects.create(
            username=user.username,
            email=user.email,
        )
        new_user.set_password(user.password)
        new_user.save()

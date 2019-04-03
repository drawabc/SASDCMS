from django.contrib.auth.decorators import user_passes_test

def user_is_staff(user):
    return user.is_staff

from account.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook' and kwargs['is_new']:
        Profile.objects.create(user=user)
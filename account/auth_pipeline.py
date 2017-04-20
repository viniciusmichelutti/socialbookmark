from django.core.files.base import ContentFile
from requests import request
from requests.exceptions import HTTPError

from account.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook' and kwargs['is_new']:
        profile = Profile.objects.create(user=user)

        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        try:
            response = request('GET', url, params={'type': 'large'})
            response.raise_for_status()
        except HTTPError:
            pass
        else:
            profile.photo.save('{0}_social.jpg'.format(user.username),
                                       ContentFile(response.content))
            profile.save()
            
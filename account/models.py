from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(to=User)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return "Profile from {user}".format(user=self.user.get_full_name())


class Contact(models.Model):
    from_user = models.ForeignKey(User, related_name='rel_from_set')
    to_user = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{} follows {}".format(self.from_user, self.to_user)


User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))

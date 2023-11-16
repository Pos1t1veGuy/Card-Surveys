from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_user.jpg')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.id:
            old_avatar = User.objects.get(pk=self.id).avatar
            if self.avatar and old_avatar != self.avatar:
                old_avatar.delete()
        super(User, self).save(*args, **kwargs)

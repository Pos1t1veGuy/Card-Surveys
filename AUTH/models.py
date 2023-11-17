from django.db import models
from django.contrib.auth.models import AbstractUser

import os


class ModelUtils:
    def filename(name: str) -> str:
        result_name = name
        count = 0

        while os.path.exists(result_name):
            filename, ext = '.'.join(result_name.split('.')[:-1]), result_name.split('.')[-1]

            if len(filename.split('_')):
                if filename.split('_')[-1].isdigit():
                    count = int(filename.split('_')[-1])+1
                    filename = '_'.join(filename.split('_')[:-1])
            
            result_name = f'{filename}_{count}.{ext}'
        
        return result_name
    
    def avatar_filename(instance, filename: str) -> str:
        return ModelUtils.filename(f'avatars/{filename}')


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=ModelUtils.avatar_filename, default='avatars/default_user.png')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.id:
            old_avatar = User.objects.get(pk=self.id).avatar
            if self.avatar and old_avatar != self.avatar:
                old_avatar.delete()
        super(User, self).save(*args, **kwargs)
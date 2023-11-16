from django.db import models
from django.db.models import JSONField
from AUTH.models import User

class Survey(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    avatar = models.ImageField(upload_to='survey_avatars/', default='survey_avatars/default_survey.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_surveys')
    participants = models.ManyToManyField(User, related_name='surveys_participant', blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.id:
            old_avatar = Survey.objects.get(pk=self.id).avatar
            if self.avatar and old_avatar != self.avatar:
                old_avatar.delete()
        super(Survey, self).save(*args, **kwargs)

class Card(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    avatar = models.ImageField(upload_to='card_avatars/', default='card_avatars/default_card.jpg')
    user_rates = JSONField(default=dict)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.id:
            old_avatar = Card.objects.get(pk=self.id).avatar
            if self.avatar and old_avatar != self.avatar:
                old_avatar.delete()
        super(Card, self).save(*args, **kwargs)

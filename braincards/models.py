from django.db import models

class CardTypes(models.TextChoices):
    YOUTUBE= "youtube", "youtube"
    TWEET= "tweet", "tweet"
    SPOTIFY= "spotify", "spotify"
    LINK= "link", "link"
    TEXT= "text", "text"


class BrainCard(models.Model):
    brain_space = models.ForeignKey('brainspaces.BrainSpace', on_delete=models.CASCADE, related_name='brain_cards')
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    card_type = models.CharField(choices=CardTypes.choices, default=CardTypes.LINK)
    tags = models.ManyToManyField('tags.Tag', blank=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_shared = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    vectoredOnData = models.TextField(blank=True)

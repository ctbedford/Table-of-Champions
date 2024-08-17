from django.db import models
from django.db.models import JSONField  # Use this import instead


class Player(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    hometown = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    first_session_date = models.DateField(blank=True, null=True)
    total_net_winnings = models.DecimalField(
        max_digits=15, decimal_places=2, default=0)
    total_episodes = models.IntegerField(default=0)
    total_hours_played = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    avg_table_bb = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    biography = models.TextField(blank=True, null=True)
    social_media_handles = JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name


class Stream(models.Model):
    name = models.CharField(max_length=255)
    logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    date = models.DateField()
    game_type = models.CharField(max_length=255)
    stakes_played = models.CharField(max_length=255)
    effective_bb = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.stream.name} - {self.date}"


class PlayerSessionStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    net_winnings = models.DecimalField(max_digits=15, decimal_places=2)
    vpip = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pfr = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    hours_played = models.DecimalField(max_digits=5, decimal_places=2)
    hourly = models.DecimalField(max_digits=10, decimal_places=2)
    bb_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('player', 'session')

    def __str__(self):
        return f"{self.player.name} - {self.session}"


class TweetTemplate(models.Model):
    content = models.TextField()
    variables = JSONField(default=dict)

    def __str__(self):
        return self.content[:50]


class ScheduledTweet(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
    ]
    template = models.ForeignKey(TweetTemplate, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.template} - {self.scheduled_time}"


class LastUpdate(models.Model):
    update_time = models.DateTimeField(auto_now=True)

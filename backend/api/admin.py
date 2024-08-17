from django.contrib import admin
from .models import Player, Stream, Session, PlayerSessionStats, TweetTemplate, ScheduledTweet

admin.site.register(Player)
admin.site.register(Stream)
admin.site.register(Session)
admin.site.register(PlayerSessionStats)
admin.site.register(TweetTemplate)
admin.site.register(ScheduledTweet)

# Register your models here.

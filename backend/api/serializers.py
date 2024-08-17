from rest_framework import serializers
from .models import Player, Stream, Session, PlayerSessionStats, TweetTemplate, ScheduledTweet, LastUpdate


class TweetTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetTemplate
        fields = ['show', 'content']


class LastUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastUpdate
        fields = ['update_time']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class PlayerSessionStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSessionStats
        fields = '__all__'


class TweetTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetTemplate
        fields = '__all__'


class ScheduledTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledTweet
        fields = '__all__'

import json
from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import TweetTemplate, LastUpdate
from .serializers import TweetTemplateSerializer, LastUpdateSerializer
from scraper.scraper import scrape_data
from twitter.tweet_post_generator import generate_tweet
from twitter.twitter_post import post_tweet


class TweetTemplateViewSet(viewsets.ModelViewSet):
    queryset = TweetTemplate.objects.all()
    serializer_class = TweetTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class LastUpdateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LastUpdate.objects.all()
    serializer_class = LastUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request):
        last_update = self.get_queryset().order_by('-update_time').first()
        if last_update:
            serializer = self.get_serializer(last_update)
            return Response([serializer.data])
        return Response([])


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def manual_post_tweet(request):
    try:
        scrape_data()
        tweet_content = generate_tweet()
        post_tweet(tweet_content)
        LastUpdate.objects.create()
        return Response({"success": True, "message": "Tweet posted successfully"})
    except Exception as e:
        return Response({"success": False, "error": str(e)})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def sync_template(request):
    show = request.data.get('show')
    try:
        template = TweetTemplate.objects.get(show=show)
        post_tweet(template.content)
        LastUpdate.objects.create()
        return Response({"success": True})
    except TweetTemplate.DoesNotExist:
        return Response({"success": False, "error": "Template not found"})
    except Exception as e:
        return Response({"success": False, "error": str(e)})


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_poker_data(request):
    try:
        with open('highroll_poker_data.json', 'r') as f:
            data = json.load(f)
        return Response(data)
    except FileNotFoundError:
        return Response({"error": "Poker data not found"}, status=404)
    except json.JSONDecodeError:
        return Response({"error": "Invalid poker data file"}, status=500)

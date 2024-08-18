from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    TweetTemplateViewSet,
    LastUpdateViewSet,
    manual_post_tweet,
    sync_template,
    get_poker_data,
)
from api.views import index


router = DefaultRouter()
router.register(r'templates', TweetTemplateViewSet)
router.register(r'last-update', LastUpdateViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('post-tweet/', manual_post_tweet, name='post-tweet'),
    path('sync-template/', sync_template, name='sync-template'),
    path('poker-data/', get_poker_data, name='get-poker-data'),
]

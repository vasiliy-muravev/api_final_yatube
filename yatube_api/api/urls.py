from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'follow', FollowViewSet, basename='followers')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]

from django.urls import path, include
from . import views
# from .views import TweetList
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers

# router = SimpleRouter()
# router.register(r'tweets', views.TweetViewSet)
# router.register(r'comments', views.CommentViewSet)

router = routers.DefaultRouter()
router.register('tweets', views.TweetViewSet, basename='tweets')

comment_router = routers.NestedDefaultRouter(router, "tweets", lookup='tweet')
comment_router.register('comments', views.CommentViewSet, basename='tweets-comments')

urlpatterns = router.urls + comment_router.urls

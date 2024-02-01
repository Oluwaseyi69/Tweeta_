from django.urls import path
from . import views
from .views import TweetList

urlpatterns = [
    path('', views.TweetList.as_view()),
    path('<int:pk>/', views.TweetDetail.as_view()),
    path('comments/<int:pk>', views.CommentList.as_view())
    # path('', views.tweets),
]
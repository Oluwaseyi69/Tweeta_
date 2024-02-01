from django.urls import path

from . import views
from tweet import views as tweet_views

app_name = 'playground'
urlpatterns = [
    path('home/', views.welcome),
    path('hello/<str:name>', views.hello),
    path('<int:number>/', views.numbers),
    # path('tweets', tweet_views.tweets)

]

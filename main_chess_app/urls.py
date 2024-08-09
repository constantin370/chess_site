from django.urls import path
from main_chess_app.views.show_news import NewsListView
from main_chess_app.views.single_news import NewsDetailView
from main_chess_app.views.show_category_view import CategoryListView
from main_chess_app.views.media_list_view import MediaListView
from main_chess_app.views.video_detail_view import VideoDetailView

app_name = "news"


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news_detail/<slug:news_slug>/', NewsDetailView.as_view(), name='single_news'),
    path('single_category/<slug:cat_slug>/', CategoryListView.as_view(), name='news_single_category'),
    path('video/', MediaListView.as_view(), name='video_list'),
    path('video/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
] 
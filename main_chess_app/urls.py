from django.urls import path
from main_chess_app.views.show_news import NewsListView
from main_chess_app.views.single_news import NewsDetailView
from main_chess_app.views.show_category_view import CategoryListView
from main_chess_app.views.videos_list_view import VideoListView
from main_chess_app.views.search_view import Search
from main_chess_app.views.homepages_view import HomepagesView
from main_chess_app.views.photo_list_view import PhotoListView
from main_chess_app.views.show_partners_logo import LogosListView
from main_chess_app.views.squad_list_views import SquadListView

app_name = "news"


urlpatterns = [
    path('', HomepagesView.as_view(), name='homepages'),
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('news_detail/<slug:news_slug>/', NewsDetailView.as_view(), name='single_news'),
    path('single_category/<slug:cat_slug>/', CategoryListView.as_view(), name='news_single_category'),
    path('video/', VideoListView.as_view(), name='video_list'),
    path('search/', Search.as_view(), name='search'),
    path('photos/', PhotoListView.as_view(), name='photo_list'),
    path('partnership/', LogosListView.as_view(), name='logo_list'),
    path('squad/', SquadListView.as_view(), name='squad_list'),
] 
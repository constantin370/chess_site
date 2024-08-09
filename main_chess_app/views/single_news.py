from django.views.generic import DetailView
from main_chess_app.models.news_model import News



class NewsDetailView(DetailView):
    """Публикация."""
    model = News
    slug_url_kwarg = "news_slug"
    template_name = "main_chess_app/single_news.html"
    context_object_name = "single_news"

    

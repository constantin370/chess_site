from django.views.generic import ListView

from main_chess_app.models.news_model import News


class NewsListView(ListView):
    """Публикации новостей на главной странице."""
    model = News
    template_name = "main_chess_app/news_pages.html"
    context_object_name = "news"
    paginate_by = 3

    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by("-time_create").select_related()
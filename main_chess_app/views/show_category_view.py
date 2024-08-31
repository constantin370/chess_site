from django.views.generic import ListView
from main_chess_app.models.news_model import News


class CategoryListView(ListView):
    """Представление списка новостей по категориям."""
    model = News
    template_name = "main_chess_app/category_list.html"
    context_object_name = "cat"
    paginate_by = 3

    def get_queryset(self, **kwargs):
        return News.objects.select_related('cat').filter(cat__slug=self.kwargs['cat_slug'], 
                                                         is_published=True)
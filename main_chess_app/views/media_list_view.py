from django.views.generic import ListView
from main_chess_app.models.media_models import Media


class MediaListView(ListView):
    """Представление списка новостей по категориям."""
    model = Media
    template_name = "main_chess_app/full_media.html"
    context_object_name = "media"
    paginate_by = 3

    def get_queryset(self, **kwargs):
        return Media.objects.all()
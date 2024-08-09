
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from main_chess_app.models.media_models import Media


class VideoDetailView(DetailView):
    """Публикация."""
    model = Media
    id_url_kwarg = "media_id"
    template_name = "main_chess_app/video_deatal.html"
    context_object_name = "video_detail"

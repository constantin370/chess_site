from django.views.generic import ListView
from main_chess_app.models.video_models import Video
from django.shortcuts import get_list_or_404

class VideoListView(ListView):
    """Представление списка видео."""
    model = Video
    template_name = "main_chess_app/video_list.html"
    context_object_name = "videos"
    paginate_by = 3

    def get_queryset(self, **kwargs):
        return get_list_or_404(Video.objects.filter(is_published=True))
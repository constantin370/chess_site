from django.views.generic import ListView
from main_chess_app.models.photo_model import Photo
from django.shortcuts import get_list_or_404


class PhotoListView(ListView):
    """Представление списка фото."""
    model = Photo
    template_name = "main_chess_app/photo_list.html"
    context_object_name = "photos"
    paginate_by = 3

    def get_queryset(self, **kwargs):
        return get_list_or_404(Photo.objects.filter(is_published=True))
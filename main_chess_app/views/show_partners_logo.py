from django.views.generic import ListView
from main_chess_app.models.logo_models import Logo
from django.shortcuts import get_list_or_404


class LogosListView(ListView):
    """Представление списка фото."""
    model = Logo
    template_name = "main_chess_app/partners_logo.html"
    context_object_name = "logos"
    paginate_by = 3

    def get_queryset(self, **kwargs):
        return get_list_or_404(Logo.objects.filter(is_published=True))
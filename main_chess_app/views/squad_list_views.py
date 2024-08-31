from django.views.generic import ListView
from django.shortcuts import get_list_or_404
from main_chess_app.models.squad_models import Squad


class SquadListView(ListView):
    """Вывод списка команды турнира."""
    model = Squad
    template_name = "main_chess_app/squad_pages.html"
    context_object_name = "squad"
    paginate_by = 3

    def get_queryset(self):
        return get_list_or_404(Squad.objects.filter(is_published=True).order_by("-time_create"))
from django.utils.datastructures import MultiValueDictKeyError
from django.http import Http404
from django.views.generic import ListView
from django.shortcuts import get_list_or_404
from main_chess_app.models.news_model import News


class Search(ListView):
    """Класс представления поиска по новостным заголовкам."""

    template_name = 'main_chess_app/news_pages.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        try:
            return get_list_or_404(News.objects.filter(is_published=True, 
                                                        title__icontains=self.request.GET.get('name_input_field')).select_related('cat'))
        except MultiValueDictKeyError:
                return get_list_or_404(News.objects.filter(is_published=True).select_related('cat'))
        except ValueError:
            return get_list_or_404(News.objects.filter(is_published=True).select_related('cat'))
        except Http404:
             raise Http404("Новости не найдены.")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_input_field'] = self.request.GET.get('name_input_field')
        return context
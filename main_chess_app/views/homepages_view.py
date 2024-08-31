from django.views.generic import View
from django.shortcuts import render


class HomepagesView(View):
    """Класс отображения главной страницы сайта."""
    template_name = 'main_chess_app/homepages.html'
    
    def get(self, request):
        return render(request, self.template_name)
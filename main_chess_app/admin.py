from django.contrib import admin
from main_chess_app.models.news_model import News
from main_chess_app.models.category_models import Category
from main_chess_app.models.video_models import Video
from main_chess_app.models.photo_model import Photo
from main_chess_app.models.logo_models import Logo
from main_chess_app.models.squad_models import Squad


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Video)
admin.site.register(Photo)
admin.site.register(Logo)
admin.site.register(Squad)
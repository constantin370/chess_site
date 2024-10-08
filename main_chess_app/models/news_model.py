from django.db import models
from django.urls import reverse


class News(models.Model):
    """Модель перечня Новостей."""
    title             = models.CharField(verbose_name='Заголовок', max_length=255)
    slug              = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content           = models.TextField(verbose_name='Текст', blank=True)
    photo             = models.ImageField(upload_to='post_images', verbose_name='Фото')
    time_create       = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update       = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    is_published      = models.BooleanField(verbose_name='Опубликовать', default=True)
    video_url_all     = models.CharField(verbose_name='Ссылка на видео', max_length=255, 
                                         default=None, blank=True, null=True)
    # Список категорий, на которые News ссылается через внешний ключ cat.
    cat = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает заголовок новости
        как ее строковое представление."""
        return self.title

    def get_absolute_url(self):
        """Метод возвращает URL страницы
        с информацией о конкретной новости."""
        return reverse('news:single_news', kwargs={'news_slug': self.slug})
    
    class Meta:
        """Для понятного отображения названий."""
        verbose_name = 'Новости'
        verbose_name_plural = 'Новость'
        ordering = ['-time_create', 'title']
from django.db import models


class Squad(models.Model):
    """Модель команды турнира."""
    title             = models.CharField(verbose_name='Заголовок', max_length=255)
    content           = models.TextField(verbose_name='Текст', blank=True)
    photo             = models.ImageField(upload_to='post_images', verbose_name='Фото')
    time_create       = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update       = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    is_published      = models.BooleanField(verbose_name='Опубликовать', default=True)

    def __str__(self):
        """Возвращает заголовок новости
        как ее строковое представление."""
        return self.title

    class Meta:
        """Для понятного отображения названий."""
        verbose_name = 'Участники'
        verbose_name_plural = 'Участник'
        ordering = ['time_create', 'title']
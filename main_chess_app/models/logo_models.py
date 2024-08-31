from django.db import models


class Logo(models.Model):
    """Модель списка логотопов партнёров."""
    title        = models.CharField(max_length=100, blank=True, null=True)
    logo         = models.ImageField(upload_to='images/', verbose_name='Фото')
    logo_url     = models.CharField(verbose_name='Ссылка на партнёра', max_length=255, 
                                         default=None, blank=True, null=True)
    time_create  = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update  = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    is_published = models.BooleanField(verbose_name='Опубликовать', default=True)

    def __str__(self):
        """Возвращает заголовок логотопов
        партнёров как ее строковое представление."""
        return f'Партнёр №{self.title}'

    class Meta:
        """Для понятного отображения логотопов партнёров."""
        verbose_name = 'Логотопы'
        verbose_name_plural = 'Лого'
        ordering = ['-time_create']
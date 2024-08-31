from django.db import models


class Photo(models.Model):
    """Модель списка фотографий."""
    title             = models.CharField(verbose_name='Нумерация фотографий', max_length=255)
    photo             = models.ImageField(upload_to='images/', verbose_name='Фото')
    time_create       = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update       = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    is_published      = models.BooleanField(verbose_name='Опубликовать', default=True)

    def __str__(self):
        """Возвращает заголовок новости
        как ее строковое представление."""
        return f'Фото №{self.title}'

    class Meta:
        """Для понятного отображения названий."""
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фото'
        ordering = ['-time_create']